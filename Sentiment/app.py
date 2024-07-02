"""
@Description :   App demo
@Author      :   Xubo Luo 
@Time        :   2024/06/29 23:04:51
"""

from Sentiment import predict
import streamlit as st

if __name__ == '__main__':
    st.title("EasyBert")
    st.write("This is a simple sentiment analysis tool based on BERT.")
    text = st.text_area("Input your text here (Ch):")
    if st.button("Predict"):
        result = predict(text)
        st.write(result)


