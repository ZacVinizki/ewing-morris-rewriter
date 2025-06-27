#!/usr/bin/env python3
"""
Quick setup script for Ewing Morris Marketing Assistant
Run this to check if everything is set up correctly
"""

import os
import sys
import subprocess

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        return False
    print(f"✅ Python {sys.version.split()[0]} - Good!")
    return True

def check_virtual_env():
    """Check if virtual environment is activated"""
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Virtual environment is activated")
        return True
    else:
        print("⚠️ Virtual environment not detected")
        print("   Run: python -m venv venv")
        print("   Then: venv\\Scripts\\activate (Windows) or source venv/bin/activate (Mac/Linux)")
        return False

def check_env_file():
    """Check if .env file exists and has API key"""
    if not os.path.exists('.env'):
        print("❌ .env file not found")
        print("   Create .env file with: OPENAI_API_KEY=your_key_here")
        return False
    
    with open('.env', 'r') as f:
        content = f.read()
        if 'OPENAI_API_KEY=' not in content or 'your_openai_api_key_here' in content:
            print("❌ .env file missing valid API key")
            print("   Add your real OpenAI API key to .env file")
            return False
    
    print("✅ .env file configured")
    return True

def check_dependencies():
    """Check if required packages are installed"""
    required = ['streamlit', 'openai', 'python-dotenv']
    missing = []
    
    for package in required:
        try:
            __import__(package.replace('-', '_'))
            print(f"✅ {package} installed")
        except ImportError:
            missing.append(package)
            print(f"❌ {package} not installed")
    
    if missing:
        print(f"   Run: pip install {' '.join(missing)}")
        return False
    return True

def main():
    """Run all checks"""
    print("🔍 Checking Ewing Morris Marketing Assistant setup...\n")
    
    checks = [
        check_python_version(),
        check_virtual_env(),
        check_env_file(),
        check_dependencies()
    ]
    
    if all(checks):
        print("\n🎉 Everything looks good! Run: streamlit run app.py")
    else:
        print("\n❌ Please fix the issues above before running the app")

if __name__ == "__main__":
    main()