import os
# Clear proxy environment variables that might interfere
for proxy_var in ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy']:
    if proxy_var in os.environ:
        del os.environ[proxy_var]

import openai
from typing import Dict, List
from config import Config

# Configure OpenAI (ADD THIS LINE)
openai.api_key = os.getenv("OPENAI_API_KEY")

class EwingMorrisVoiceSystem:
    """Advanced Ewing Morris voice replication system with category-specific training"""
    
    def __init__(self):
        # EXACT copy from working app
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            
        self.model = "gpt-3.5-turbo"  # Same as working app
        self.max_tokens = 1500
        self.temperature = 0.7  # Same as working app
        self.voice_examples = self._load_voice_examples()
    
    def _load_voice_examples(self) -> Dict[str, List[str]]:
        """Load categorized Ewing Morris voice examples"""
        return {
            "Newsletter Content": [
                """Welcome to the inaugural edition of The Ewing Morris Quarterly Review.
In this quarterly newsletter, our aim is to provide you with thoughtful insights, strategic updates, and a closer look at the opportunities that shape our investment approach. At Ewing Morris, we believe that true partnership is built on transparency, trust, and a shared commitment to success. This quarterly review is designed to keep you informed about the evolving market landscape and how we are positioning your portfolios to navigate it. We hope you find this review both insightful and engaging.

If this is not of interest, please feel free to unsubscribe using the link below. Otherwise, please don't hesitate to reply to this email with any feedback you may have.

Warm Regards,
Darcy Morris""",
                
                """Opportunities in an Evolving Market

In a time of global political shifts and economic uncertainty, navigating the markets requires more than just reacting to trends—it demands a disciplined, fundamentals-driven approach. At Ewing Morris, we remain focused on helping you preserve and grow your wealth, regardless of market cycles.

In this edition of the EM Quarterly Review, we explore how we build all-weather investment portfolios designed to withstand volatility and capture long-term opportunities.

Markets will always ebb and flow, but our commitment remains the same: identifying overlooked opportunities, protecting your capital, and positioning you to thrive—no matter what the future holds.

Thank you for being part of the journey.

Darcy Morris
Co-Founder and CEO"""
            ],
            
            "Event Invitations": [
                """Join us for a special pop-up election edition of our Innovator Speaker Series. We're delighted to welcome Andrew Coyne, widely regarded as Canada's foremost political commentator, for an insightful discussion on the upcoming federal election. This is a unique opportunity to hear Coyne's perspectives on the key issues influencing the election and the future of our country. **Seating is limited. Please RSVP below to secure your spot.**""",
                
                """Ewing Morris is embarking on an inspired new chapter to better serve our clients. Join us this November in Toronto as we kick off this exciting new era. At this year's Annual Investor Day we will be showcasing the evolution underway including how we will be elevating the experience we deliver both to our clients and across our network."""
            ],
            
            "Business Updates": [
                """Dear Ewing Morris Friends and Limited Partners,
In our latest update, we provide more information on our acquisition of Aventine Investment Counsel, and our efforts to bring greater value and opportunity to each of our clients.
Should you have any questions, please reach out to Will Jones at williamjones@ewingmorris.com or Darcy Morris at darcymorris@ewingmorris.com. 
Best regards, Ewing Morris & Co. Investment Partners Ltd."""
            ],
            
            "Holiday/Seasonal": [
                """As the holiday season is upon us, we at Ewing Morris want to extend our warmest wishes to you and your families. We hope you have a wonderful time filled with joy and cherished moments.

We would also like to remind you of our upcoming family-friendly Holiday Skate this Saturday. Bring the whole family to enjoy some fun on the ice, sip hot chocolate and connect with others.

We look forward to connecting with you in the New Year and wish you all the very best this holiday season!"""
            ],
            
            "Annual Letters": [
                """Dear Ewing Morris Friends and Limited Partners,
 
Our journey continues to be one of innovation, resilience, and unwavering dedication to our principles. What began 13 years ago with two lawn chairs and a vision has now grown into a robust investment platform managing ~$950 million in assets. While the milestones are gratifying, the relationships we've built and the values we've upheld are what truly matter.
 
Warm Regards,
Ewing Morris & Co. Investment Partners Ltd."""
            ],
            
            "Company Milestones": [
                """One of the key highlights from our recent Investor Day was the remarkable journey of Ewing Morris. As we enter our 14th year of operation, we take immense pride in the growth and achievements we've accomplished together. We are eagerly anticipating even greater opportunities to serve our clients and friends as we look ahead to the promising year of 2025. **The Ewing Morris Team**"""
            ]
        }
    
    def _create_ewing_morris_prompt(self, original_content: str, category: str) -> str:
        """ Create professional and conversational, friendly Ewing Morris voice prompts using the examples above and following that style"""
        
        examples = self.voice_examples.get(category, [])
        
        # Voice characteristics for each category
        voice_profile = {
            "Newsletter Content": {
                "tone": "Friendly expert sharing insights, conversational but smart",
                "style": "Brief sections, easy to scan, personal touch from leadership",
                "language": "Simple 'we think', 'here's what we're seeing', expertise"
            },
            "Event Invitations": {
                "tone": "Excited and welcoming, like inviting a client over for drinks",
                "style": "Key details, why it's special, easy RSVP",
                "language": "We hope that you join us, hope to have a great experience, looking forward to see you"
            },
            "Business Updates": {
                "tone": "Quick and friendly update, like texting a professional buisness partner the news",
                "style": "Here's what happened, why it matters, any questions just ask",
                "language": "Casual but very professional, brief and clear and to the point, no fluff"
            },
            "Holiday/Seasonal": {
                "tone": "Warm and genuine, like a note from a lawyer to a friend",
                "style": "Short and concise, event details, we are looking forward to seeing you",
                "language": "Hope you're well, can't are looking forward to seeing you, wishing you and your family a wonderful holiday season"
            },
            "Annual Letters": {
                "tone": "Personal reflection, like a year-end chat with friends",
                "style": "Brief highlights, professional and relatively serious tone, excited about what's next",
                "language": "It's been quite a year, with several ups and downs we have overcame the problems that came our way, excited about ahead"
            },
            "Company Milestones": {
                "tone": "Excited to share good news, humble but proud and super professional no matter what",
                "style": "Quick celebration, thank you, looking ahead together",
                "language": "Pretty amazing milestone, we wanted to thank you all as we wouldn't have been able to achieve such milestones without your help"
            }
        }
        
        category_profile = voice_profile.get(category, voice_profile["Newsletter Content"])
        
        prompt = f"""IGNORE THE WRITING STYLE AND TONE OF THE INPUT COMPLETELY.

Your job: 
1. Extract ONLY the facts/purpose from the input text
2. Write NEW content in Ewing Morris voice using those facts

EWING MORRIS VOICE = FRIENDLY + SMART + BRIEF
• Talk like you're having coffee with a smart friend
• No corporate jargon or fluff - just genuine, helpful content always being professional
• Family and relationship focused, we want to make it feel personalized while being very professional and not even remotely silly, immature, or childish
• Keep it short and conversational and to the point

CONTENT TYPE: {category}
VOICE FOR THIS TYPE: {category_profile['tone']}
WRITING STYLE: {category_profile['style']}
LANGUAGE TONE: {category_profile['language']}

HERE'S HOW EWING MORRIS ACTUALLY WRITES FOR {category}:
"""
        
        for i, example in enumerate(examples[:2], 1):
            prompt += f"\n--- Example {i} ---\n{example}\n"
        
        prompt += f"""

EWING MORRIS STYLE RULES:
✓ Write like a smart, analytical, and professional human, not a press release
✓ Keep it brief - people are busy
✓ Be friendly but professional and not overly friendly
✓ Use "we" and "you" - make it personal
✓ No unnecessary fancy terminology or jargon
✓ Use simple, clear language - no fluff
✓ Show you care about people, not just business
✓ Confident but not arrogant

CRITICAL: DO NOT copy the style/tone of the input. Extract facts only, then write in Ewing Morris voice.

INPUT TEXT (extract facts only, ignore style):
{original_content}

STEP 1: What are the key facts/purpose from this input?
STEP 2: Now write this in authentic Ewing Morris voice using the examples above.

NEW CONTENT IN EWING MORRIS VOICE:"""
        
        return prompt
    
    def rewrite_content(self, original_content: str, category: str) -> str:
        """Rewrite content using advanced Ewing Morris voice replication"""
        try:
            prompt = self._create_ewing_morris_prompt(original_content, category)
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": """You are an Ewing Morris communication specialist. Your job is to:

1. EXTRACT the core facts/purpose from any input text
2. COMPLETELY IGNORE the input's writing style, tone, and language choices
3. GENERATE fresh content in consistent Ewing Morris voice

NEVER copy or be influenced by the input's style. Whether the input is overly formal, casual, fancy, or simple - you always output the same consistent Ewing Morris voice. Think 'smart friend having coffee' not 'corporate press release'. Keep it brief, genuine, and human."""
                    },
                    {"role": "user", "content": prompt}
                ],
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            
            return response.choices[0].message.content.strip() # type: ignore
            
        except Exception as e:
            print(f"Full error details: {e}")
            return f"Error rewriting content: {str(e)}"
