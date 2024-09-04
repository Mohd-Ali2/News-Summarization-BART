# News Summarization

This project extracts text from a news article URL and provides a summarized version of the article using a transformer model. The summarization process is implemented using the Hugging Face `transformers` library and the `facebook/bart-large-cnn` model. The web interface is built with Streamlit.

## Features

- **Extracts Text**: Retrieves and extracts text from news articles by scraping paragraphs from a given URL.
- **Summarizes**: Uses the BART model to generate a summary of the extracted text.
- **Web Interface**: A user-friendly web application built with Streamlit to input URLs and view summaries.

## Requirements

- Python 3.6 or later
- `requests` - For making HTTP requests to fetch the news article
- `beautifulsoup4` - For parsing HTML and extracting text
- `transformers` - For text summarization using BART model
- `streamlit` - For creating the web application

## Installation

1. Clone the repository:

   ```bash
   https://github.com/Mohd-Ali2/News-Summarization-BART.git

2. Navigate to directory

   ```bash
   cd News-Summarization-BART

4. Install the required packages

   ```bash
   pip install requests beautifulsoup4 transformers streamlit keras-tf

6. Run it.

   ```bash
   streamlit run app.py
