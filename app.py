import streamlit as st
import requests

st.set_page_config(page_title="FRIDAY")
st.title("F.R.I.D.A.Y - AI 🤖")
st.write("Python + Google Cloud se bana hai Boss!")

# Chabi Cloud ke Secret se aayegi, Code me nahi likhi hai
api_key = st.secrets.get("GOOGLE_API_KEY", "")

sawal = st.text_input("Kuch bhi pucho Boss:")

if st.button("PUCHO"):
    if not api_key:
        st.error("Cloud me Secret me Key nahi dali Boss!")
    elif not sawal:
        st.error("Pehle sawal likho Boss!")
    else:
        with st.spinner("Soach rahi hu..."):
            try:
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-lite:generateContent?key={api_key}"
                res = requests.post(url, json={"contents": [{"parts": [{"text": sawal}]}]})
                data = res.json()
                if "error" in data:
                    st.error(f"ERROR: {data['error']['message']}")
                else:
                    jawab = data["candidates"][0]["content"]["parts"][0]["text"]
                    st.success(jawab)
            except Exception as e:
                st.error(f"ERROR: {e}")
