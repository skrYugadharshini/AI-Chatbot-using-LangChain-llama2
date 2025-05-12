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
