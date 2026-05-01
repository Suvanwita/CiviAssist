import streamlit as st
from rag_engine import get_recommendations

st.set_page_config(page_title="BIS Recommendation Engine")

st.title("🏗️ BIS Standards Recommendation Engine")
st.write("Enter a product description to find relevant BIS standards")

query = st.text_input("🔍 Product Description")

if st.button("Get Recommendations"):
    if query:
        retrieved, answer = get_recommendations(query)

        st.subheader("📌 Top Matches")
        for doc in retrieved[:5]:
            st.write(f"**{doc['id']} - {doc['title']}**")
            st.write(f"Scope: {doc['scope']}")
            st.write(f"Confidence: {doc['score']:.2f}")
            st.markdown("---")

        st.subheader("🤖 AI Explanation")
        st.write(answer)