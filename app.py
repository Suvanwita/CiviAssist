import streamlit as st
from rag_engine import get_recommendations
import time

suggestions = [
    "IS code for cement",
    "Concrete mix design IS code",
    "Standard for reinforced concrete",
    "IS code for steel reinforcement",
    "Aggregates standard in construction"
]

st.set_page_config(page_title="BIS Recommendation Engine")

st.title("🏗️ BIS Standards Recommendation Engine")
st.write("Enter a product description to find relevant BIS standards")

if "query" not in st.session_state:
    st.session_state.query = ""

st.sidebar.title("💡 Suggested Queries")
for i in range(0, len(suggestions), 2):
    col1, col2 = st.sidebar.columns(2)
    
    if i < len(suggestions):
        if col1.button(suggestions[i]):
            st.session_state.query = suggestions[i]
            st.rerun()
    
    if i + 1 < len(suggestions):
        if col2.button(suggestions[i + 1]):
            st.session_state.query = suggestions[i + 1]
            st.rerun()

query = st.text_input("🔍 Product Description", value=st.session_state.query)

if st.button("Get Recommendations"):
    if query:
        with st.spinner("⚡ Analyzing query and retrieving standards..."):
            time.sleep(1)
            retrieved, answer = get_recommendations(query)

        st.subheader("📌 Top Matches")
        for doc in retrieved[:5]:
            st.write(f"**{doc['id']} - {doc['title']}**")
            st.write(f"Scope: {doc['scope']}")
            st.write(f"Confidence: {doc['score']:.2f}")
            st.markdown("---")

        st.subheader("🤖 AI Explanation")
        st.write(answer)