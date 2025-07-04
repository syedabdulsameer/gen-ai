import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def enhance_caption(caption: str, tone: str = "natural and expressive") -> str:
    prompt = f"Rewrite this caption in a more {tone} way:\n\"{caption}\""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a caption improver."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception:
        return caption