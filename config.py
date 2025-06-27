import os
from pathlib import Path
from dotenv import load_dotenv

# More robust environment loading
def load_environment():
    """Load environment variables from .env file with multiple fallback locations"""
    
    possible_paths = [
        '.env',  # Current directory
        Path(__file__).parent / '.env',  # Same directory as this file
        Path(__file__).parent.parent / '.env',  # Parent directory
    ]
    
    for env_path in possible_paths:
        if os.path.exists(env_path):
            load_dotenv(env_path)
            print(f"✅ Config: Loaded environment from {env_path}")
            return True
    
    print("❌ Config: No .env file found in any expected location")
    return False

# Load environment variables
load_environment()

class Config:
    """Configuration class to manage all app settings"""
    
    # API Configuration
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    
    # Debug output
    if OPENAI_API_KEY:
        print(f"✅ Config: API key loaded successfully ({OPENAI_API_KEY[:20]}...)")
    else:
        print("❌ Config: No API key found in environment variables")
        print("Available env vars:", [k for k in os.environ.keys() if 'OPENAI' in k.upper()])
    
    # Model Configuration
    OPENAI_MODEL = "gpt-3.5-turbo"  # Using working model
    MAX_TOKENS = 1500
    TEMPERATURE = 0.7
    
    # App Configuration
    APP_TITLE = "Ewing Morris Marketing Assistant"
    APP_ICON = "🎯"
    
    @classmethod
    def validate_config(cls):
        """Validate that required configuration is present"""
        if not cls.OPENAI_API_KEY:
            raise ValueError(
                f"OpenAI API key not found. Please check your .env file. "
                f"Current working directory: {os.getcwd()}"
            )
        return True
    
    @staticmethod
    def get_openai_config():
        """Get OpenAI configuration including project ID support"""
        return {
            "api_key": os.getenv("OPENAI_API_KEY"),
            "project_id": os.getenv("OPENAI_PROJECT_ID"),
            "model": "gpt-4",
            "max_tokens": 1500,
            "temperature": 0.3
        }