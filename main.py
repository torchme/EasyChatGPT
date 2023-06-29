import streamlit as st
import gpt4all

if __name__ == "__main__":
    st.title("Chatbot")
    with st.spinner("Loading model..."):
        gptj = gpt4all.GPT4All("orca-mini-3b.ggmlv3.q4_0")


    with st.chat_message("EasyChatGPT"):
        st.write("Hello, how I can help you?")


    prompt = st.chat_input('Say something:')
    if prompt:
        with st.chat_message("User"):
            st.write(prompt)
        response = [{"role": "user", "content": prompt}]
        answer = gptj.chat_completion(response)
        answer = answer['choices'][0]['message']['content']
        with st.chat_message("EasyChatGPT"):
            st.write(answer)
