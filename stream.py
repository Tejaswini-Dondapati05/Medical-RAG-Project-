import streamlit as st
import requests

st.set_page_config(
    page_title="Medical RAG Assistant",
    page_icon="🏥"
)

st.title("🏥 Medical RAG Assistant")
st.write("Ask questions from your medical documents")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
question = st.chat_input("Ask your medical question...")

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        try:
            response = requests.post(
                "http://127.0.0.1:8000/ask",
                json={"question": question},
                timeout=180
            )

            response.raise_for_status()

            data = response.json()

            answer = data.get("answer", str(data))

            st.write(answer)

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })

        except requests.exceptions.RequestException as e:
            st.error(f"Backend Error: {e}")