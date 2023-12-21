import streamlit as st
import google.generativeai as palm

# Configure the generative AI model
palm.configure(api_key="AIzaSyDv_I3QM9Rd06G9nSSMXLOtolcXFqWvlVI")

# Default parameters for the generative AI model
defaults = {
    'model': 'models/chat-bison-001',
    'temperature': 0.25,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
}

# Page title with styling
st.title("Make Your Body Email")
st.markdown("---")  # Add a horizontal line for separation

# Streamlit chat input for email context
prompt = st.text_area("Enter the context for the email:", height=100)

# Placeholder examples and messages
examples = []
messages = []
messages.append("NEXT REQUEST")

# Button to trigger response generation
if st.button("Generate Email Body"):
    if prompt:
        # Limit input to 50 words
        input_text = ' '.join(prompt.split()[:50])
        
        # Check if the first word is "make" or "write"
        first_word = input_text.lower().split()[0]
        if first_word not in ['make', 'write']:
            st.warning("Please start your input with 'make' or 'write'.")
        else:
            examples.append({"input": input_text, "output": {"content": "Placeholder content"}})

            response = palm.chat(
                **defaults,
                context=input_text,
                examples=examples,
                messages=messages
            )

            print("Model Response:", response.last)  # Add this line to print the model response
            if response.last is not None:
                 styled_output = f'<div style="background-color: #304D30; padding: 10px; color: white;">{response.last}</div>'
                 st.write(styled_output, unsafe_allow_html=True)
            else:
                st.warning("I can only generate responses related to the body of an email.")

# User instruction for English input
st.markdown("**Note:** Please enter your context in English and the initial word must use make or write")
