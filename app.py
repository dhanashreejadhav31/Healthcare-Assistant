import streamlit as st 
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')


chatbot = pipeline("text-generation",model="distilgpt2")

def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        return "Please consult doctor for accurate advice"
    elif  "appointment" in user_input:
        return "would you like to schedule appointment with the doctor?"
    elif "medication" in user_input:
        return "It's important to take prescribed medicines regularly. If you have concerns,consult your doctor."
    elif "diet" in user_input or "healthy food" in user_input:
        return """A healthy daily diet includes:
        - 🥦 Plenty of vegetables and fruits
        - 🍞 Whole grains (brown rice, oats, quinoa)
        - 🥩 Lean protein (chicken, fish, beans)
        - 🥑 Healthy fats (olive oil, nuts, seeds)
        - 💧 Stay hydrated with at least 8 glasses of water """

    else:
        response = chatbot(user_input,max_length = 500,num_return_sequences=1)
    return response[0]['generated_text']
def main():
    st.title("Healthcare Assistent Chatbot")
    user_input = st.text_input("How can I assist you today?")
    if st.button("submit"):
        if user_input:
            st.write("User :",user_input)
            with st.spinner("Processing your query ,please  wait...."):
                 response=healthcare_chatbot(user_input)
            st.write("Healthcare Assistant: ",response)
            print(response)
        else:
            st.write("Please enter a message to get a response.")    


main()    