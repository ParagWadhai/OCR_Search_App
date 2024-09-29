import streamlit as st
import easyocr
from PIL import Image
import io

@st.cache_resource
def load_ocr():
    return easyocr.Reader(['en', 'hi'])  # Load for English and Hindi

def perform_ocr(image):
    reader = load_ocr()
    result = reader.readtext(image)
    return ' '.join([text for _, text, _ in result])

def search_text(text, query):
    return text.lower().find(query.lower()) != -1

st.title('OCR and Text Search App')

uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Perform OCR
    with st.spinner('Performing OCR...'):
        text = perform_ocr(image)
    
    st.subheader("Extracted Text:")
    st.write(text)
    
    # Search functionality
    search_query = st.text_input("Enter search term:")
    if search_query:
        if search_text(text, search_query):
            st.success(f"Found '{search_query}' in the text!")
            # Highlight the search term in the text
            highlighted_text = text.replace(search_query, f"**{search_query}**")
            st.markdown(highlighted_text)
        else:
            st.warning(f"'{search_query}' not found in the text.")

st.markdown("---")
st.markdown("Created with Streamlit and EasyOCR")