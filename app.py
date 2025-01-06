from dotenv import load_dotenv
load_dotenv()  ## Load all environment variables

import streamlit as st
import os
import sqlite3
import google.generativeai as genai
import pandas as pd

# Configure our API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini model and provide query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to retrieve query from the SQL database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    df = pd.read_sql_query(sql, conn)
    conn.close()
    return df

prompt = [
    """
    You are an advanced language model capable of translating plain English questions into efficient SQL query.
    The SQL Database has name STUDENT and has following columns - NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT.
    Guidelines:
    Focus only on read operations (e.g., SELECT statements).
    Do not include any comments or formatting markers (e.g., no triple backticks around SQL code).
    Ensure the query is valid and follows standard SQL conventions.
    Handle scenarios like filtering, sorting, and aggregation based on the English question.
    Provide only the query as output; avoid additional explanations.
    The output query should not mention ''' character in the end or beginning, as well as sql word throughout the query
    Examples:

    Input 1:
    Retrieve all the student names and their marks.
    Output 1:
    SELECT NAME, MARKS FROM STUDENT;

    Input 2:
    Get the name and class of the student with the highest marks.
    Output 2:
    SELECT NAME, CLASS FROM STUDENT WHERE MARKS = (SELECT MAX(MARKS) FROM STUDENT);

    Input 3:
    List all students in section 'B', ordered by their marks in descending order.
    Output 3:
    SELECT * FROM STUDENT WHERE SECTION = 'B' ORDER BY MARKS DESC;

    Input 4:
    Find the average marks of students in section 'C'.
    Output 4:
    SELECT AVG(MARKS) AS AVERAGE_MARKS FROM STUDENT WHERE SECTION = 'C';

    Input 5:
    Retrieve the number of students who scored less than 50 marks.
    Output 5:
    SELECT COUNT(*) AS STUDENT_COUNT FROM STUDENT WHERE MARKS < 50;
    """
]

## Streamlit App

st.set_page_config(page_title="Text To SQL query")
st.header("Gemini App to Retrieve SQL Data")

question = st.text_input("Input: ", key="input")

submit = st.button("Ask Question")

# If submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    st.subheader("Generated SQL Query:")
    st.code(response, language='sql')
    
    # Fetch data and display in table format
    data = read_sql_query(response, "student.db")
    st.subheader("Query Result:")
    st.table(data)
