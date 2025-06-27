# Ewing Morris Marketing Assistant

A friendly AI-powered tool that rewrites content in Ewing Morris's authentic voice.

## 🚀 Setup

1. **Clone/download this project**
2. **Create virtual environment**: 
   ```bash
   python -m venv venv
   ```
3. **Activate it**: 
   ```bash
   # Windows:
   venv\Scripts\activate
   
   # Mac/Linux:
   source venv/bin/activate
   ```
4. **Install dependencies**: 
   ```bash
   pip install -r requirements.txt
   ```
5. **Create `.env` file** with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_actual_api_key_here
   ```
6. **Run the app**: 
   ```bash
   streamlit run app.py
   ```

## ✨ Features

- Rewrites content in authentic Ewing Morris voice
- Multiple content categories (newsletters, events, business updates, etc.)
- Before/after comparison view
- Download results as text files
- Beautiful dark theme UI
- Secure API key handling

## 📁 Project Structure

```
ewing-morris-assistant/
├── app.py              # Main Streamlit application
├── config.py           # Configuration and settings
├── voice_system.py     # AI voice rewriting logic
├── styles.py          # CSS styling
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (API keys)
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## 🌐 Deployment

Deploy to:
- **Streamlit Cloud**: Connect your GitHub repo
- **Heroku**: Add Procfile with `web: streamlit run app.py --server.port=$PORT`
- **Railway**: Automatic deployment from GitHub
- **Local Network**: Perfect for team internal use

## 🔧 Customization

- Modify voice examples in `voice_system.py`
- Adjust styling in `styles.py`
- Add new content categories in the voice examples
- Tweak AI parameters in `config.py`

## 🛠️ Troubleshooting

- **API Key Error**: Make sure your `.env` file has the correct OpenAI API key
- **Import Errors**: Ensure virtual environment is activated and dependencies installed
- **Port Issues**: Streamlit runs on port 8501 by default

## 📞 Support

Built with ❤️ for the Ewing Morris marketing team.