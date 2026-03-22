import streamlit as st
# from snowflake.snowpark.context import get_active_session

# Get Snowflake session

cnx = st.connection("Snowflake")
session = cnx.session()

# UI Title
st.title("Customize Your Smoothie! 🥤")
st.write("Choose the fruits you want in your custom Smoothie!")

# Name input (MISSING IN YOUR CODE)
name_on_order = st.text_input("Name on Smoothie:")

if name_on_order:
    st.write(f"The name on your Smoothie will be: {name_on_order}")

# Load table
my_dataframe = session.table("smoothies.public.fruit_options")

# Convert to list
fruit_list = [row["FRUIT_NAME"] for row in my_dataframe.collect()]

# Multiselect
ingredients_list = st.multiselect(
    "Choose up to 5 ingredients:",
    fruit_list
)

# Process selection
if ingredients_list:
    ingredients_string = " ".join(ingredients_list)

    # Button (must come BEFORE execution)
    time_to_insert = st.button("Submit Order")

    if time_to_insert:
        # Clean SQL
        my_insert_stmt = f"""
            INSERT INTO smoothies.public.orders (ingredients, name_on_order)
            VALUES ('{ingredients_string}', '{name_on_order}')
        """

        session.sql(my_insert_stmt).collect()
        st.success("Your Smoothie is ordered! ✅")

import requests  
smoothiefroot_response = requests.get("[https://my.smoothiefroot.com/api/fruit/watermelon](https://my.smoothiefroot.com/api/fruit/watermelon)")  
st.text(smoothiefroot_response)
