import os
from dotenv import load_dotenv
import openai

load_dotenv()

def check_openai_account():
    """Comprehensive OpenAI account checker"""
    
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("❌ No API key found in .env file")
        return
    
    print(f"🔑 Testing API key: {api_key[:20]}...")
    
    try:
        client = openai.OpenAI(api_key=api_key)
        
        # Test 1: Simple completion
        print("\n🧪 Test 1: Simple API call...")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello"}],
            max_tokens=5
        )
        print("✅ API call successful!")
        print(f"Response: {response.choices[0].message.content}")
        
    except openai.AuthenticationError as e:
        print("❌ AUTHENTICATION ERROR")
        print(f"Details: {e}")
        print("\n🔧 This usually means:")
        print("   • Invalid API key")
        print("   • API key doesn't have permission")
        print("   • Wrong organization/project")
        
    except openai.PermissionDeniedError as e:
        print("❌ PERMISSION DENIED")
        print(f"Details: {e}")
        print("\n🔧 This usually means:")
        print("   • No billing set up")
        print("   • Insufficient credits")
        print("   • Account restrictions")
        
    except openai.RateLimitError as e:
        print("❌ RATE LIMIT ERROR")
        print(f"Details: {e}")
        print("\n🔧 This usually means:")
        print("   • You've hit your usage quota")
        print("   • Too many requests too quickly")
        
    except openai.APIError as e:
        print("❌ API ERROR")
        print(f"Details: {e}")
        print("\n🔧 This could be:")
        print("   • Temporary OpenAI service issue")
        print("   • Model not available")
        
    except Exception as e:
        print(f"❌ UNEXPECTED ERROR: {e}")
        print(f"Error type: {type(e)}")

if __name__ == "__main__":
    print("🚀 OpenAI Account Diagnostic Tool")
    print("=" * 40)
    check_openai_account()
    print("\n" + "=" * 40)
    print("🌐 Check your account at: https://platform.openai.com/")
    print("💳 Billing: https://platform.openai.com/settings/organization/billing")
    print("📊 Usage: https://platform.openai.com/usage")