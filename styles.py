def get_custom_css():
    """Gradually built-up complex CSS without phantom text area issues"""
    return """
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Main app background and typography */
    .stApp {
        background: linear-gradient(135deg, #0c0c0c 0%, #1a1a1a 50%, #0c0c0c 100%);
        font-family: 'Inter', sans-serif;
        color: white;
    }
    
    /* Main container */
    .main .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
        max-width: 1000px !important;
    }
    
    /* Custom header styling */
    .header-section {
        text-align: center;
        margin-bottom: 3rem;
        padding: 2rem 0;
    }
    
    .main-title {
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #64b5f6 0%, #42a5f5 50%, #2196f3 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
        text-shadow: 0 0 30px rgba(100, 181, 246, 0.3);
    }
    
    .subtitle {
        font-size: 1.2rem;
        color: #e0e0e0;
        font-weight: 300;
        margin-bottom: 0.5rem;
    }
    
    .description {
        font-size: 1rem;
        color: #b0b0b0;
        font-weight: 400;
        max-width: 600px;
        margin: 0 auto;
        line-height: 1.6;
    }
    
    /* Main card container */
    .main-card {
        background: rgba(15, 25, 35, 0.95);
        border: 2px solid rgba(100, 181, 246, 0.3);
        border-radius: 25px;
        padding: 4rem;
        margin: 2rem 0;
        box-shadow: 0 25px 60px rgba(0, 0, 0, 0.4), 
                    0 0 0 1px rgba(100, 181, 246, 0.2),
                    inset 0 2px 0 rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        position: relative;
        overflow: hidden;
    }
    
    .main-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at 20% 20%, rgba(100, 181, 246, 0.05) 0%, transparent 50%),
                    radial-gradient(circle at 80% 80%, rgba(33, 150, 243, 0.05) 0%, transparent 50%);
        pointer-events: none;
    }
    
    /* Section headers */
    .section-header {
        font-size: 1.8rem;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 2rem;
        text-align: center;
        text-shadow: 0 0 20px rgba(255, 255, 255, 0.3),
                     0 0 40px rgba(100, 181, 246, 0.2);
        letter-spacing: 0.5px;
    }
    
    .section-subheader {
        font-size: 1.3rem;
        font-weight: 500;
        color: #ffffff;
        margin-bottom: 2rem;
        text-align: center;
        text-shadow: 0 0 15px rgba(255, 255, 255, 0.2);
        letter-spacing: 0.3px;
    }
    
    /* Progress step indicator */
    .progress-step {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        background: linear-gradient(135deg, #64b5f6 0%, #2196f3 100%);
        color: #ffffff;
        font-weight: 700;
        font-size: 1.5rem;
        margin: 0 auto 2rem auto;
        box-shadow: 0 0 30px rgba(100, 181, 246, 0.7);
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
    }
    
    /* SAFE Text Area styling - no complex selectors */
    .stTextArea textarea {
        background: rgba(15, 25, 35, 0.95) !important;
        border: 2px solid rgba(100, 181, 246, 0.5) !important;
        border-radius: 15px !important;
        color: #ffffff !important;
        font-size: 1.1rem !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 400 !important;
        padding: 1.5rem !important;
        transition: all 0.3s ease !important;
        backdrop-filter: blur(15px) !important;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4), 
                    inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.1) !important;
    }
    
    .stTextArea textarea:focus {
        border-color: #64b5f6 !important;
        box-shadow: 0 0 30px rgba(100, 181, 246, 0.6), 
                    0 8px 25px rgba(0, 0, 0, 0.4),
                    inset 0 1px 0 rgba(255, 255, 255, 0.2) !important;
        outline: none !important;
        transform: translateY(-2px) !important;
    }
    
    .stTextArea textarea::placeholder {
        color: rgba(255, 255, 255, 0.6) !important;
        font-style: italic !important;
    }
    
    /* SAFE Button styling - simplified selectors */
    .stButton button {
        background: linear-gradient(135deg, #64b5f6 0%, #2196f3 50%, #1976d2 100%) !important;
        border: none !important;
        border-radius: 15px !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 1.2rem !important;
        padding: 1rem 2rem !important;
        transition: all 0.4s ease !important;
        box-shadow: 0 8px 25px rgba(100, 181, 246, 0.4),
                    0 0 0 1px rgba(255, 255, 255, 0.2),
                    inset 0 1px 0 rgba(255, 255, 255, 0.3) !important;
        width: 100% !important;
        height: 70px !important;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.3) !important;
        letter-spacing: 0.5px !important;
        position: relative !important;
        overflow: hidden !important;
    }
    
    .stButton button:hover {
        transform: translateY(-3px) scale(1.02) !important;
        box-shadow: 0 15px 40px rgba(100, 181, 246, 0.6),
                    0 0 0 2px rgba(255, 255, 255, 0.3),
                    inset 0 2px 0 rgba(255, 255, 255, 0.4) !important;
        background: linear-gradient(135deg, #42a5f5 0%, #1976d2 50%, #0d47a1 100%) !important;
    }
    
    /* Shimmer effect on buttons */
    .stButton button::before {
        content: '' !important;
        position: absolute !important;
        top: 0 !important;
        left: -100% !important;
        width: 100% !important;
        height: 100% !important;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent) !important;
        transition: left 0.5s ease !important;
    }
    
    .stButton button:hover::before {
        left: 100% !important;
    }
    
    /* Loading animation */
    .loading-container {
        text-align: center;
        padding: 4rem 2rem;
        background: rgba(10, 20, 30, 0.95);
        border-radius: 20px;
        border: 2px solid rgba(100, 181, 246, 0.5);
        margin: 2rem 0;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4),
                    0 0 0 1px rgba(100, 181, 246, 0.2);
        backdrop-filter: blur(20px);
        position: relative;
        overflow: hidden;
    }
    
    .loading-text {
        color: #ffffff;
        font-size: 1.4rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        text-shadow: 0 0 20px rgba(100, 181, 246, 0.5),
                     0 0 40px rgba(255, 255, 255, 0.2);
        letter-spacing: 0.5px;
        position: relative;
        z-index: 1;
    }
    
    .loading-subtext {
        color: rgba(255, 255, 255, 0.8);
        font-size: 1.1rem;
        font-style: italic;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.1);
        position: relative;
        z-index: 1;
    }
    
    .spinner {
        border: 4px solid rgba(100, 181, 246, 0.2);
        border-top: 4px solid #64b5f6;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        animation: spin 1s linear infinite;
        margin: 2rem auto;
        box-shadow: 0 0 20px rgba(100, 181, 246, 0.4);
        position: relative;
        z-index: 1;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* Success container */
    .success-container {
        background: rgba(10, 30, 20, 0.95);
        border: 2px solid rgba(76, 175, 80, 0.6);
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4);
        backdrop-filter: blur(15px);
    }
    
    .success-text {
        color: #ffffff;
        font-size: 1.3rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 0 0 15px rgba(76, 175, 80, 0.5);
        letter-spacing: 0.5px;
    }
    
    /* Result container */
    .result-container {
        background: rgba(10, 20, 30, 0.95);
        border: 2px solid rgba(100, 181, 246, 0.6);
        border-radius: 20px;
        padding: 2.5rem;
        margin: 2rem 0;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.5),
                    0 0 0 1px rgba(100, 181, 246, 0.3),
                    inset 0 2px 0 rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        position: relative;
        overflow: hidden;
    }
    
    .result-text {
        color: #ffffff;
        font-size: 1.2rem;
        line-height: 1.8;
        font-weight: 400;
        margin-bottom: 1.5rem;
        text-shadow: 0 0 15px rgba(255, 255, 255, 0.2);
        letter-spacing: 0.3px;
        position: relative;
        z-index: 1;
    }
    
    /* Info/Success messages */
    .stInfo {
        background: rgba(10, 25, 40, 0.95) !important;
        border-left: 4px solid #64b5f6 !important;
        color: #ffffff !important;
        text-shadow: 0 0 8px rgba(255, 255, 255, 0.1) !important;
    }
    
    .stSuccess {
        background: rgba(15, 40, 20, 0.95) !important;
        border: 2px solid rgba(76, 175, 80, 0.6) !important;
        border-radius: 12px !important;
        color: #ffffff !important;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.1) !important;
        animation: successPulse 0.5s ease !important;
    }
    
    @keyframes successPulse {
        0% { transform: scale(0.95); opacity: 0; }
        50% { transform: scale(1.02); }
        100% { transform: scale(1); opacity: 1; }
    }
    
    /* Download button styling */
    .stDownloadButton button {
        background: linear-gradient(135deg, #9c27b0 0%, #673ab7 100%) !important;
        border: none !important;
        border-radius: 12px !important;
        color: #ffffff !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        padding: 0.8rem 1.5rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 6px 20px rgba(156, 39, 176, 0.3) !important;
        text-shadow: 0 0 8px rgba(255, 255, 255, 0.2) !important;
    }
    
    .stDownloadButton button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(156, 39, 176, 0.4) !important;
    }
    
    /* Disabled text areas */
    .stTextArea textarea:disabled {
        background: rgba(25, 35, 45, 0.95) !important;
        border: 2px solid rgba(100, 181, 246, 0.3) !important;
        color: rgba(255, 255, 255, 0.9) !important;
        opacity: 1 !important;
        text-shadow: 0 0 8px rgba(255, 255, 255, 0.1) !important;
    }
    
    /* Code blocks */
    .stCode {
        background: rgba(10, 20, 30, 0.95) !important;
        border: 2px solid rgba(100, 181, 246, 0.4) !important;
        border-radius: 12px !important;
        color: #ffffff !important;
        padding: 1.5rem !important;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.1) !important;
    }
</style>
"""