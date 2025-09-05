from fastapi import FastAPI
from pydantic import BaseModel
from Task1.image_generator.image_gen import generate_image
import os 
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins=[
    "http://localhost:8501",
    "http://127.0.0.1:8501"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ImageRequest(BaseModel):
    prompt: str

@app.post("/generate-image/")
def generate_image_endpoint(request: ImageRequest):
    image_path = generate_image.invoke(request.prompt)  
    image_id = os.path.basename(image_path)
    return {
        "image_id": image_id,
        "image_url": f"/image/{image_id}"
    }

@app.get("/image/{image_id}")
def get_image(image_id: str):
    image_path = os.path.join("images", image_id)
    if os.path.exists(image_path):
        return FileResponse(image_path, media_type="image/png")
    return {"error": "Image not found"}
