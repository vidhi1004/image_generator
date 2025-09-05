from langchain.tools import tool
from huggingface_hub import InferenceClient
import os, uuid
from dotenv import load_dotenv
load_dotenv()
client = InferenceClient(token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"))

IMAGE_DIR = "images"
os.makedirs(IMAGE_DIR, exist_ok=True)

@tool
def generate_image(prompt: str) -> str:
    """Generate an image from a text prompt and return its file path"""
    result = client.text_to_image(
        prompt,
        model="stabilityai/stable-diffusion-3.5-large",
        negative_prompt="blurry, low quality",
    )
    
    img = result 

    image_id = str(uuid.uuid4()) + ".png"
    image_path = os.path.join(IMAGE_DIR, image_id)
    img.save(image_path)
    return image_path