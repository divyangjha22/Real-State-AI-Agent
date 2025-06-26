import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from newspaper import Article
import pytesseract
from pdf2image import convert_from_path
from abc import ABC, abstractmethod

class BaseScraper(ABC):

    def __init__(self, base_dir="../data"):
        self.base_dir = base_dir
        os.makedirs(self.base_dir, exist_ok=True)
        print(f"[INIT] Base directory created/set: {self.base_dir}")

    @abstractmethod
    def scrape(self):
        """Main method to perform scraping"""
        pass

    def _make_dir(self, subdir):
        """Helper method to create directories"""
        path = os.path.join(self.base_dir, subdir)
        os.makedirs(path, exist_ok=True)
        print(f"[DIR] Directory created/set: {path}")
        return path

class OCRConverter(BaseScraper):
    """Converter for PDF to text using OCR"""

    def __init__(self, base_dir="data"):
        super().__init__(base_dir)
        self.input_dir = os.path.join(self.base_dir, "raw/zoning_pdfs")
        self.output_dir = os.path.join(self.base_dir, "processed/ocr_text")
        self._make_dir("raw/zoning_pdfs")
        self._make_dir("processed/ocr_text")

    def _convert_pdf_to_text(self, pdf_path):
        """Convert a single PDF to text using OCR"""
        print(f"[OCR] Converting PDF: {pdf_path}")
        images = convert_from_path(pdf_path)
        text = ""
        for i, image in enumerate(images):
            print(f"  - Processing page {i + 1}")
            text += pytesseract.image_to_string(image) + "\n"
        return text

    def scrape(self):
        """Main method to process all PDFs in input directory"""
        print("[START] OCR PDF Conversion")
        for pdf_file in os.listdir(self.input_dir):
            if pdf_file.endswith(".pdf"):
                full_path = os.path.join(self.input_dir, pdf_file)
                output_file = os.path.join(self.output_dir, pdf_file.replace(".pdf", ".txt"))

                text = self._convert_pdf_to_text(full_path)

                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(text)

                print(f"[DONE] OCR complete for {pdf_file} → {output_file}")

class ArticleScraper(BaseScraper):
    """Scraper for architecture articles"""

    def __init__(self, base_dir="data"):
        super().__init__(base_dir)
        self.raw_dir = os.path.join(self.base_dir, "raw/articles")
        self._make_dir("raw/articles")
        self.sources = {
            "archdaily": "https://www.archdaily.com",
            "designboom": "https://www.designboom.com/architecture/",
        }

    def _get_article_links(self, base_url, keyword_filter="architecture"):
        """Fetch article links from a given source"""
        print(f"[FETCH] Article links from: {base_url}")
        response = requests.get(base_url)
        soup = BeautifulSoup(response.text, "html.parser")
        links = []

        for a_tag in soup.find_all("a", href=True):
            href = a_tag['href']
            full_url = urljoin(base_url, href)
            if keyword_filter in href and full_url not in links:
                links.append(full_url)

        print(f"[FOUND] {len(links)} links from {base_url}")
        return list(set(links))

    def _fetch_and_save_article(self, url, source_name, index):
        """Fetch and save a single article"""
        try:
            print(f"  - Fetching article: {url}")
            article = Article(url)
            article.download()
            article.parse()

            if article.text.strip():
                file_path = os.path.join(self.raw_dir, f"{source_name}_{index}.txt")
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(article.title + "\n\n" + article.text)

                print(f"  ✓ Saved article to: {file_path}")
                return True

        except Exception as e:
            print(f"  ✗ Failed to fetch {url}: {e}")
            return False

    def scrape(self):
        """Main method to scrape articles from all sources"""
        print("[START] Article Scraping")
        for name, base_url in self.sources.items():
            links = self._get_article_links(base_url)
            for i, url in enumerate(links):
                self._fetch_and_save_article(url, name, i)

class DataScraper:
    """Main class to coordinate all scraping activities"""

    def __init__(self, base_dir="data"):
        self.ocr_converter = OCRConverter(base_dir)
        self.article_scraper = ArticleScraper(base_dir)

    def run_all(self):
        """Run all scrapers in sequence"""

        print("🚀 Starting All Scraping Tasks")

        print("\n Starting PDF to Text OCR Conversion...")
        self.ocr_converter.scrape()

        print("\n[2] Starting Article Scraping...")
        self.article_scraper.scrape()

        print("\n✅ All scraping tasks completed!")

if __name__ == "__main__":
    scraper = DataScraper()
    scraper.run_all()
