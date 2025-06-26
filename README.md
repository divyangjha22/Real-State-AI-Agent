# 🏠 AI Real Estate Agent Pro

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32%2B-FF4B4B)](https://streamlit.io/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-0.4.15-success)](https://www.trychroma.com/)
[![Groq](https://img.shields.io/badge/Groq-API-orange)](https://groq.com/)
[![LangChain](https://img.shields.io/badge/LangChain-0.1.12-yellowgreen)](https://python.langchain.com/)

An intelligent AI assistant for real estate professionals and home buyers/sellers, providing property insights, market analysis, and investment recommendations.

## ✨ Features

- 🔍 Natural language property search
- 📈 Automated market trend analysis
- 💲 AI-powered property valuation
- 📑 Contract/document understanding
- 🏙️ Neighborhood comparison tools
- 🤖 Personalized recommendations

## 🚀 Quick Start

1. Clone the repo:

git clone https://github.com/your-username/real-estate-ai.git
cd real-estate-ai

2. Set up ENvironment:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

3. Install Dependencies:

pip install -r requirements.txt

4. Create .env file:

GROQ_API_KEY=your_api_key_here
MAPBOX_TOKEN=your_mapbox_key

5. Run the Application:

streamlit run webapp/app.py

## 📂 Project Structure

real-estate-ai/
├── data/                   # Property data storage
│   ├── raw/                # Original data files
│   └── processed/          # Cleaned and processed data
├── database/               # Vector database setup
├── modules/                # Core functionality modules
├── webapp/                 # Streamlit application
├── scripts/                # Data processing scripts
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

## 🤖 Core Technologies

- AI Backend: Groq + Llama 3 70B
- Vector Database: ChromaDB
- Embeddings: BAAI/bge-small-en
- Frontend: Streamlit
- Geospatial: Mapbox + Geopandas

## 📝 Usage Examples

- Find properties: "Show me 3-bedroom homes under $500k with good schools"
- Market analysis: "What's the price trend in Downtown last 6 months?"
- Valuation: "Estimate value for 123 Main St based on comps"

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create your feature branch
3. Submit a pull request

## 📄 License
MIT License - See LICENSE for details.

<div align="center"> 💡 Making real estate smarter with AI </div> ```