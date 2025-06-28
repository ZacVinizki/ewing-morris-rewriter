import os
import sys
from pathlib import Path

# More robust environment loading
# More robust environment loading with project key support
try:
    from dotenv import load_dotenv
    
    # Try loading from current directory first
    if os.path.exists('.env'):
        load_dotenv('.env')
        print("✅ Loaded .env from current directory")
    else:
        # Try loading from script directory
        script_dir = Path(__file__).parent
        env_path = script_dir / '.env'
        if env_path.exists():
            load_dotenv(env_path)
            print(f"✅ Loaded .env from {env_path}")
        else:
            print("❌ No .env file found")
    
    # Debug output for API key and project ID
    api_key = os.getenv("OPENAI_API_KEY")
    project_id = os.getenv("OPENAI_PROJECT_ID")
    
    if api_key:
        print(f"✅ API key loaded: {api_key[:20]}...")
        if api_key.startswith('proj-'):
            print("📋 Project-scoped key detected")
            if project_id:
                print(f"✅ Project ID loaded: {project_id}")
                # Ensure environment variables are set for OpenAI client
                os.environ["OPENAI_API_KEY"] = api_key
                os.environ["OPENAI_PROJECT_ID"] = project_id
            else:
                print("⚠️  Project key found but no OPENAI_PROJECT_ID set")
        else:
            # Regular API key
            os.environ["OPENAI_API_KEY"] = api_key
    else:
        print("❌ No API key found in environment")
        
except Exception as e:
    print(f"❌ Error loading environment: {e}")

import streamlit as st
import time
from datetime import datetime
from config import Config
from voice_system import EwingMorrisVoiceSystem
from styles import get_custom_css

# Configure the page
st.set_page_config(
    page_title="Ewing Morris Marketing Assistant",
    page_icon="🎯",
    layout="wide"
)

# Apply custom CSS
st.markdown(get_custom_css(), unsafe_allow_html=True)

# Initialize session state
def init_session_state():
    if 'step' not in st.session_state:
        st.session_state.step = 1
    if 'user_text' not in st.session_state:
        st.session_state.user_text = ""
    if 'content_purpose' not in st.session_state:
        st.session_state.content_purpose = ""
    if 'rewritten_content' not in st.session_state:
        st.session_state.rewritten_content = ""
    if 'selected_purpose' not in st.session_state:
        st.session_state.selected_purpose = None

def render_header():
    """Render the application header"""
    st.markdown("""
    <div class="header-section">
        <div class="main-title">Ewing Morris Marketing Team Assistant</div>
        <div class="subtitle">Make any text sound like us</div>
        <div class="description">Friendly, conversational, and authentically Ewing Morris</div>
    </div>
    """, unsafe_allow_html=True)

def render_step_1():
    """Render the content input and purpose selection step"""
    st.markdown("""
    <div class="progress-step">1</div>
    <div class="section-header">What do you want to rewrite?</div>
    """, unsafe_allow_html=True)
    
    user_text = st.text_area(
        "Text Input",
        height=200,
        placeholder="Paste your text here and we'll make it sound like Ewing Morris...\n\nCould be anything - email drafts, social posts, newsletter ideas, whatever you're working on!",
        key="text_input",
        label_visibility="collapsed"
    )
    
    st.markdown('<div class="section-subheader">What kind of content is this?</div>', unsafe_allow_html=True)
    
    # Purpose options
    purpose_options = [
        {"id": "newsletter", "icon": "📧", "title": "Newsletter Content", "desc": "Quarterly reviews and comprehensive updates"},
        {"id": "events", "icon": "🎯", "title": "Event Invitations", "desc": "Speaker series, investor days, holiday events"},
        {"id": "business", "icon": "📋", "title": "Business Updates", "desc": "Company news and brief announcements"},
        {"id": "holiday", "icon": "🎉", "title": "Holiday/Seasonal", "desc": "Warm community messages and celebrations"},
        {"id": "annual", "icon": "📈", "title": "Annual Letters", "desc": "Personal, reflective CEO messages"},
        {"id": "milestones", "icon": "🏆", "title": "Company Milestones", "desc": "Achievements and journey highlights"}
    ]
    
    # Create 2x3 grid for purpose selection
    for row in range(2):
        cols = st.columns(3)
        for col_idx, col in enumerate(cols):
            option_idx = row * 3 + col_idx
            if option_idx < len(purpose_options):
                option = purpose_options[option_idx]
                with col:
                    is_selected = st.session_state.selected_purpose == option['title']
                    button_style = "🟦 " if is_selected else ""
                    
                    if st.button(
                        f"{button_style}{option['icon']} **{option['title']}**\n\n{option['desc']}", 
                        key=f"purpose_{option['id']}",
                        use_container_width=True,
                        type="primary" if is_selected else "secondary"
                    ):
                        st.session_state.selected_purpose = option['title']
                        st.rerun()
    
    # Show selection status
    if st.session_state.selected_purpose:
        st.success(f"✅ Selected: {st.session_state.selected_purpose}")
    
    # Process button
    if st.button("✨ Make it sound like Ewing Morris"):
        if not user_text.strip():
            st.error("❌ Paste some text first!")
        elif not st.session_state.selected_purpose:
            st.error("❌ Pick a content type above")
        else:
            st.session_state.user_text = user_text.strip()
            st.session_state.content_purpose = st.session_state.selected_purpose
            st.session_state.step = 2
            st.rerun()

def render_step_2():
    """Render the processing/loading step"""
    st.markdown("""
    <div class="loading-container">
        <div class="progress-step">2</div>
        <div class="loading-text">Making this sound like Ewing Morris...</div>
        <div class="spinner"></div>
        <div class="loading-subtext">Adding that friendly, conversational touch</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Simulate processing time
    time.sleep(2)
    
    # Process with Ewing Morris voice system
    try:
        voice_system = EwingMorrisVoiceSystem()
        result = voice_system.rewrite_content(
            st.session_state.user_text,
            st.session_state.content_purpose
        )
        st.session_state.rewritten_content = result
        st.session_state.step = 3
        st.rerun()
    except Exception as e:
        print("OPENAI ERROR:", e)
        st.error(f"❌ Error: {str(e)}")
        st.error("Check your OpenAI billing and API key")
        if st.button("🔙 Go Back"):
            st.session_state.step = 1
            st.rerun()

def render_step_3():
    """Render the results step - SIMPLE WORKING COPY"""
    st.markdown("""
    <div class="success-container">
        <div class="progress-step">3</div>
        <div class="success-text">✨ Perfect! Now it sounds like Ewing Morris</div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.rewritten_content:
        # Display the content in a nice container
        st.markdown(f"""
        <div class="result-container">
            <div class="result-text">{st.session_state.rewritten_content}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Action buttons
        col1, col2, col3 = st.columns(3)
        
        with col1:
            copy_clicked = st.button("📋 Copy")
        
        with col2:
            st.download_button(
                "💾 Download",
                data=st.session_state.rewritten_content,
                file_name=f"ewing_morris_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
                mime="text/plain"
            )
        
        with col3:
            if st.button("🔄 New"):
                st.session_state.step = 1
                st.session_state.user_text = ""
                st.session_state.rewritten_content = ""
                st.session_state.selected_purpose = None
                st.rerun()
        
        # Show copy area when copy button is clicked
        if copy_clicked:
            st.success("✅ Textdef render_step_3():
    """Render the results step - ACTUALLY WORKING COPY"""
    st.markdown("""
    <div class="success-container">
        <div class="progress-step">3</div>
        <div class="success-text">✨ Perfect! Now it sounds like Ewing Morris</div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.rewritten_content:
        # Display the content in a nice container
        st.markdown(f"""
        <div class="result-container">
            <div class="result-text">{st.session_state.rewritten_content}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Action buttons
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📋 Copy"):
                st.balloons()
                st.success("✅ Use the copy button in the code box below:")
                st.code(st.session_state.rewritten_content, language=None)
        
        with col2:
            st.download_button(
                "💾 Download",
                data=st.session_state.rewritten_content,
                file_name=f"ewing_morris_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
                mime="text/plain"
            )
        
        with col3:
            if st.button("🔄 New"):
                st.session_state.step = 1
                st.session_state.user_text = ""
                st.session_state.rewritten_content = ""
                st.session_state.selected_purpose = None
                st.rerun()
    
    # Show comparison
    with st.expander("🔍 See Before & After"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**What You Wrote:**")
            st.text_area("Original", value=st.session_state.user_text, height=150, disabled=True, key="orig_compare")
        
        with col2:
            st.markdown("**Ewing Morris Version:**")
            st.text_area("Rewritten", value=st.session_state.rewritten_content, height=150, disabled=True, key="new_compare")

def render_footer():
    """Render the application footer"""
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; margin-top: 3rem; padding: 2rem; color: #666;">
        <strong>Ewing Morris Marketing Assistant</strong> • Making everything sound like us • Built with ❤️ for the team
    </div>
    """, unsafe_allow_html=True)

def main():
    """Main application function"""
    init_session_state()
    
    render_header()
    
    # Route to appropriate step
    if st.session_state.step == 1:
        render_step_1()
    elif st.session_state.step == 2:
        render_step_2()
    elif st.session_state.step == 3:
        render_step_3()
    
    render_footer()

if __name__ == "__main__":
    main()