# src/medical_bot.py (Final Streaming Version)

from openai import OpenAI
import base64
import io
from PIL import Image
import pydicom
import numpy as np

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OPENROUTER_MODEL = "meta-llama/llama-4-maverick:free"

DISCLAIMER = (
    "**IMPORTANT DISCLAIMER:** I am an AI assistant and not a medical professional. "
    "This analysis is for information purposes only and MUST NOT be used for diagnosis "
    "or replace consultation with a real healthcare provider.\n\n"
)

class MedicalVisionBot:
    def __init__(self, api_key: str):
        self.client = OpenAI(
            api_key=api_key,
            base_url=OPENROUTER_BASE_URL
        )
        self.model = OPENROUTER_MODEL

    def _encode_image(self, image_bytes: bytes) -> str | None:
        try:
            try:
                dcm = pydicom.dcmread(io.BytesIO(image_bytes))
                arr = dcm.pixel_array
                
                if arr.dtype != np.uint8 and arr.max() > 0:
                     arr = ((arr - arr.min()) / (arr.max() - arr.min())) * 255
                     arr = arr.astype(np.uint8)

                img = Image.fromarray(arr)
                buf = io.BytesIO()
                img.save(buf, "PNG") 
                image_bytes = buf.getvalue()
            except Exception:
                pass
            
            encoded = base64.b64encode(image_bytes).decode("utf-8")
            return encoded
        except Exception as e:
            print(f"Image encoding error: {e}")
            return None

    def analyze_stream(self, image_bytes: bytes | None, query: str):
        """
        Sends the user's query and optional image to the vision model and yields chunks.
        """
        try:
            encoded = None
            if image_bytes:
                encoded = self._encode_image(image_bytes)
                if not encoded:
                    raise ValueError("Unreadable or unsupported image format.")

            system_content = DISCLAIMER + "Describe visible medical patterns clearly, safely, and professionally. Maintain a highly professional and cautious tone. Always re-state the disclaimer."
            
            user_content = [{"type": "text", "text": query}]
            if encoded:
                user_content.append({
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{encoded}"
                    }
                })

            messages = [
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content}
            ]

            stream = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=800,
                temperature=0.1,
                timeout=30,
                stream=True
            )

            for chunk in stream:
                content = chunk.choices[0].delta.content
                if content:
                    yield {"success": True, "chunk": content}

        except Exception as e:
            error_message = f"API or Chat Completion Error: {e}"
            print(error_message)
            yield {"success": False, "error": error_message}