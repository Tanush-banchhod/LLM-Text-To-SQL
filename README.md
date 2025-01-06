# LLM-Text-To-SQL

## Overview

LLM-Text-To-SQL leverages a Large Language Model (LLM) to convert natural language questions into SQL queries. This application uses a pre-trained generative model to translate user queries into SQL commands, which are then executed on a SQLite database to retrieve the desired information.

## Features

- **Natural Language Processing:** Converts plain English questions into efficient SQL queries.
- **Database Interaction:** Executes generated SQL queries on a SQLite database.
- **Streamlit Integration:** Provides a user-friendly web interface to interact with the model and database.
- **Environment Variable Management:** Utilizes `dotenv` to manage API keys and other sensitive information.

## Prerequisites

- Python 3.9 or higher
- `pip` for package management
- SQLite for the database

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Tanush-banchhod/LLM-Text-To-SQL.git
   cd LLM-Text-To-SQL
    ```
2. **Create and activate a virtual environment:**
   ```bash
     python -m venv myenv
     .\myenv\Scripts\activate  # On Windows
     source myenv/bin/activate  # On macOS/Linux
    ```
3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
    ```
4. **Create a `.env` file:**
   ```bash
   touch .env
    ```
  - Add your environment variables (e.g., API keys) to the .env file:
      ```bash
      GOOGLE_API_KEY=your_google_api_key
      ```

### Usage
1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Navigate to the local URL provided by Streamlit (e.g.,`http://localhost:8501`) to access the application.

3. Enter your natural language question into the input box and click the "Ask Question" button.

4. The application will display the generated SQL query and the query results in a tabular format.

### Sample Questions
Here are some example questions you can ask:

1. Retrieve all the student names and their marks.

2. Get the name and class of the student with the highest marks.

3. List all students in section 'B', ordered by their marks in descending order.

4. Find the average marks of students in section 'C'.

5. Retrieve the number of students who scored less than 50 marks.

### Advanced Queries
Test the application with advanced queries:

1. Retrieve the names of students who scored above 85 marks, along with their class and section.

2. Find the average marks of students in each section and sort the results by section.

3. List all students who are in the 'A' class and order them by their marks in ascending order.

4. Get the count of students in each class.

5. Find the total number of students who have scored between 70 and 90 marks.

### Contributing
Contributions are welcome! If you'd like to contribute, please fork the repository and create a pull request with your changes.

### Acknowledgements
 - Thanks to the developers of Streamlit, SQLite, and Python for providing the tools to create this project.

 - Special thanks to Google for providing the generative AI model used in this application.
