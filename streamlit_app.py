import streamlit
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt") 

streamlit.title("My Mom's New Halthy Diner")
streamlit.header('Breakfast Favourites')
streamlit.text(' 🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
#,['Avocado','Strawberries'])


# Display the table on the page.
streamlit.dataframe(my_fruit_list)

fruits_to_show = my_fruit_list.loc(fruits_selected)

#streamlit.dataframe(fruits_to_show)




