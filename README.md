# AI Image Generator with Stable Diffusion 🎨

This project is an AI-powered image generator that uses the Hugging Face Inference API to run the Stable Diffusion model. This approach allows you to generate high-quality images from text prompts without needing to download and run the large model on your local machine.

## ✨ Features

-   **Text-to-Image Generation:** Create images from any text description you can imagine.
-   **Powered by Stable Diffusion:** Leverages a state-of-the-art model for high-quality image generation.
-   **Lightweight & Efficient:** Uses the Hugging Face Inference API, so no local GPU is required.
-   **Simple Web Interface:** An easy-to-use application built with Streamlit.
-   **Image History:** Automatically saves all generated images in the `images` directory.

## 🛠️ How It Works

The application uses a Streamlit frontend (`app.py`) to capture a user's text prompt. This prompt is then sent to the Hugging Face Inference API using a personal access token. The API runs the Stable Diffusion model and returns the generated image, which is then displayed in the web app and saved locally.

## ▶️ Getting Started

### Prerequisites

-   Python 3.8+
-   A [Hugging Face](https://huggingface.co/) account and a User Access Token with `read` permissions. You can get one from your account settings.

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/image_generator.git](https://github.com/your-username/image_generator.git)
    cd image_generator
    ```

2.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up your environment variables:**
    Create a file named `.env` in the project's root directory and add your Hugging Face token:
    ```
    HUGGINGFACEHUB_API_TOKEN="your_hugging_face_token_here"
    ```

### Running the Application

1.  **Run the Streamlit Frontend:**
    ```bash
    streamlit run app.py
    ```
2.  **The web app will open in your browser, usually at `http://127.0.0.1:8501`.**

## 💻 Technologies Used

-   **Frontend:** Streamlit
-   **AI & Image Generation:** Hugging Face Inference API (Stable Diffusion)
-   **Image Handling:** Pillow (PIL)
