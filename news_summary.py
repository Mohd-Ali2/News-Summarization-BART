import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.find_all('p')
    article_text = ' '.join([para.text for para in paragraphs])
    return article_text

from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_length=1500, min_length=50):
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

import streamlit as st

st.title("News Summarization")

url = st.text_input("Enter the URL of the news article")
if st.button("Summarize"):
    if url:
        article_text = extract_text_from_url(url)
        summary = summarize_text(article_text)
        st.write("Summary:")
        st.write(summary)
