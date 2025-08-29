import streamlit as st
import psycopg2
import pandas as pd
from db import get_connection

st.title("Hello world")


# Initialize connection from render db
conn = get_connection()
cur = conn.cursor()

# Fetch data form render db
cur.execute("SELECT * FROM users;")
data = cur.fetchall()

# Call the columns from db
columns = [desc[0] for desc in cur.description]

# Display the data
df = pd.DataFrame(data, columns=columns)
st.dataframe(df)