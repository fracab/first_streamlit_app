import streamlit

streamlit.title('My parents new healthy diner')
streamlit.header('This is an header')
streamlit.text('This is text \n new line')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
