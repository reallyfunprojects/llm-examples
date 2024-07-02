import streamlit as st
import openai

st.title("🦜🔗 Langchain - Blog Outline Generator App")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

def blog_outline(topic):
    # Check if the OpenAI API key is set
    if not openai_api_key:
        return st.error("Please provide a valid OpenAI API key.")
    
    # Set the OpenAI API key
    openai.api_key = openai_api_key
    
    # Define the prompt
    prompt = f"As an experienced data scientist and technical writer, generate an outline for a blog about {topic}."
    
    try:
        # Generate a response using the OpenAI API
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=prompt,
            max_tokens=200,
            n=1,
            stop=None,
            temperature=0.7,
        )
        
        # Extract and display the response text
        outline = response.choices[0].text.strip()
        st.info(outline)
    except Exception as e:
        st.error(f"An error occurred: {e}")

with st.form("myform"):
    topic_text = st.text_input("Enter topic:", "")
    submitted = st.form_submit_button("Submit")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    elif submitted:
        blog_outline(topic_text)
