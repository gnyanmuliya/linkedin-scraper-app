import streamlit as st
import requests
import json
from datetime import datetime

# Page setup
st.set_page_config(page_title="LinkedIn Scraper API", layout="wide")
st.markdown("<h1 style='text-align:center; color:#0077B5;'>🔗 LinkedIn Profile Scraper</h1>", unsafe_allow_html=True)
st.markdown("---")

# Input section
linkedin_url = st.text_input("Enter LinkedIn Profile URL", placeholder="https://www.linkedin.com/in/username")
submit = st.button("Scrape Profile")

# Relevance AI API endpoint
API_URL = "https://api-d7b62b.stack.tryrelevance.com/latest/studios/734525c2-feb4-4c23-9b8b-5deceaca65e2/trigger_webhook?project=ddf1c035-3282-44f9-a0ad-4b7cfa8766c0"

def is_valid_linkedin_url(url):
    return any(p in url.lower() for p in ["linkedin.com/in/", "linkedin.com/company/"])

# Trigger on submit
if submit:
    if not linkedin_url:
        st.error("⚠️ Please enter a LinkedIn URL.")
    elif not is_valid_linkedin_url(linkedin_url):
        st.error("❌ Invalid LinkedIn URL.")
    else:
        with st.spinner("Scraping LinkedIn profile..."):
            try:
                response = requests.post(
                    API_URL,
                    headers={"Content-Type": "application/json"},
                    data=json.dumps({"url": linkedin_url})
                )
                if response.status_code == 200:
                    data = response.json()
                    st.success("✅ Profile scraped successfully!")
                    st.info(f"Scraped at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                    st.markdown("### 🔍 Raw Response")
                    st.json(data)
                else:
                    st.error(f"❌ Error: {response.status_code}")
                    st.text(response.text)
            except Exception as e:
                st.error(f"❌ Request failed: {e}")
