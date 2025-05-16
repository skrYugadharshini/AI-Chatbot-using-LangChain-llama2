import os
from constants import groq_key
from langchain_groq import ChatGroq
import streamlit as st

# Set the Groq API Key in the environment
os.environ["GROQ_API_KEY"] = groq_key

# Initialize the Streamlit app
st.title("LangChain + Groq (LLaMA3) Demo")

# Add input field for user to type
input_text = st.text_input("Enter your text here")

# Initialize the Groq model (LLaMA3)
llm = ChatGroq(temperature=0.8, model_name="llama3-70b-8192")

# Show a loading spinner while waiting for the response
if input_text:
    with st.spinner('Processing your request...'):
        try:
            # Get the full response from the model
            response = llm.invoke(input_text)

            # Display the full raw response for debugging
            st.write("Full raw response:")
            st.json(response)  # This will show the whole response as JSON
            
            # Try to access the 'choices' or similar structure
            if isinstance(response, dict):
                # Check for 'choices' key or nested content
                if "choices" in response:
                    choices = response.get("choices", [])
                    if choices:
                        st.write("Generated content: ", choices[0].get("text", "No text found"))
                    else:
                        st.write("No choices found in the response.")
                else:
                    st.write("No 'choices' key found. Check the raw response above.")
            else:
                st.write("Response is not in expected format. Here's the raw output:", response)

        except Exception as e:
            # Handle errors gracefully and display a message
            st.error(f"An error occurred: {str(e)}")
# Show a loading spinner while waiting for the response
if input_text:
    with st.spinner('Processing your request...'):
        try:
            # Get the full response from the model
            response = llm.invoke(input_text)

            # Display the full raw response for debugging
            st.write("Full raw response:")
            st.json(response)  # This will show the whole response as JSON
            
            # Try to access the 'choices' or similar structure
            if isinstance(response, dict):
                # Check for 'choices' key or nested content
                if "choices" in response:
                    choices = response.get("choices", [])
                    if choices:
                        st.write("Generated content: ", choices[0].get("text", "No text found"))
                    else:
                        st.write("No choices found in the response.")
                else:
                    st.write("No 'choices' key found. Check the raw response above.")
            else:
                st.write("Response is not in expected format. Here's the raw output:", response)

        except Exception as e:
            # Handle errors gracefully and display a message
            st.error(f"An error occurred: {str(e)}")
import os
from constants import groq_key
from langchain_groq import ChatGroq
import streamlit as st

# Set the Groq API Key in the environment
os.environ["GROQ_API_KEY"] = groq_key

# Initialize the Streamlit app
st.title("LangChain + Groq (LLaMA3) Demo")

# Add input field for user to type
input_text = st.text_input("Enter your text here")

# Initialize the Groq model (LLaMA3)
llm = ChatGroq(temperature=0.8, model_name="llama3-70b-8192")

# Show a loading spinner while waiting for the response
if input_text:
    with st.spinner('Processing your request...'):
        try:
            # Get the full response from the model
            response = llm.invoke(input_text)

            # Display the full raw response for debugging
            st.write("Full raw response:")
            st.json(response)  # This will show the whole response as JSON
            
            # Try to access the 'choices' or similar structure
            if isinstance(response, dict):
                # Check for 'choices' key or nested content
                if "choices" in response:
                    choices = response.get("choices", [])
                    if choices:
                        st.write("Generated content: ", choices[0].get("text", "No text found"))
                    else:
                        st.write("No choices found in the response.")
                else:
                    st.write("No 'choices' key found. Check the raw response above.")
            else:
                st.write("Response is not in expected format. Here's the raw output:", response)

        except Exception as e:
            # Handle errors gracefully and display a message
            st.error(f"An error occurred: {str(e)}")
# Show a loading spinner while waiting for the response
if input_text:
    with st.spinner('Processing your request...'):
        try:
            # Get the full response from the model
            response = llm.invoke(input_text)

            # Display the full raw response for debugging
            st.write("Full raw response:")
            st.json(response)  # This will show the whole response as JSON
            
            # Try to access the 'choices' or similar structure
            if isinstance(response, dict):
                # Check for 'choices' key or nested content
                if "choices" in response:
                    choices = response.get("choices", [])
                    if choices:
                        st.write("Generated content: ", choices[0].get("text", "No text found"))
                    else:
                        st.write("No choices found in the response.")
                else:
                    st.write("No 'choices' key found. Check the raw response above.")
            else:
                st.write("Response is not in expected format. Here's the raw output:", response)

        except Exception as e:
            # Handle errors gracefully and display a message
            st.error(f"An error occurred: {str(e)}")
