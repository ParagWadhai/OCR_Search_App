# Hindi-English OCR Web Application

![Streamlit OCR](https://www.onlineocr.net/images/scan_ocr.webp)

## Project Overview
This web-based prototype allows users to upload an image with text in Hindi and English, extract the text using Optical Character Recognition (OCR), and search for keywords within the extracted text. The application is built with Streamlit and PyTesseract, and deployed online for public access.

## Features
- Upload image in JPEG or PNG formats.
- Perform OCR on images containing both Hindi and English text.
- Basic keyword search functionality to find specific text in the OCR result.
- Simple, user-friendly interface.

## Live Demo
Check out the live application (https://ocrsearchapp-mqrfnj4m2idjwbqdnqxirs.streamlit.app/)

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ocr-web-app.git
   cd ocr-web-app

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv ocr_env
   source ocr_env/bin/activate  # On Windows use ocr_env\Scripts\activate

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

4. Run the Streamlit app locally:
   ```bash
   streamlit run ocr_app.py


