import streamlit as st 
import requests

FASTAPI_URL="http://localhost:8000"

st.title("Image Generator")
prompt=st.text_input("Enter your prompt:")
if st.button("Generate Image"):
    if prompt:
        with st.spinner("Generating image...."):
            response=requests.post(f"{FASTAPI_URL}/generate-image",json={"prompt":prompt})
            if response.status_code==200:
                data=response.json()
                image_url=data["image_url"]
                st.image(f"{FASTAPI_URL}{image_url}")
                st.success("Image generated successfully!")
            else:
                st.error("Error generating image.")