import google.generativeai as genai
import streamlit as st

genai.configure(api_key="AIzaSyC1B3zDW4G19olwgTz368YgS-ZARqzsEFE")

system_prompt="you are a python code reviewer. so you have to act as a reviewr to python code given you as an input.Youu have to generate output which shows the mistakes in a code and also generatae a correct code.If anyonw ask or pass anything other then python code then you have to reply them to pass only python code as an input."

gemini=genai.GenerativeModel(model_name="models/gemini-2.0-flash-exp",system_instruction=system_prompt)

st.title("Python Code Reviewer")
user_prompt=st.text_area(label="Enter your code here:",placeholder="Type your query here...")

btn_click=st.button("Generate answer")
# pass the user prompt to the model
if btn_click==True:
    response =  gemini.generate_content(user_prompt)
    st.write(response.text)