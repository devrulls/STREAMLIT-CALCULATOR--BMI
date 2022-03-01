import streamlit as st
from PIL import Image


st.title("Hello devRulls")
st.header("this is a header")
st.subheader("this is a subheader")

st.success("success")
st.info("information")
st.warning("warning")
st.error("error")

img = Image.open("./image/streamlit.png")

st.image(img, width=200)

if st.checkbox("Show/Hide"):
    st.text("Showing the widget")

status = st.radio("Select Gender: ", ('Male', 'Female'))

if status == 'Male':
    st.success("Male")
else:
    st.success("Female")

hobby = st.selectbox("Hobbies: ",
                     ['Dancing', 'Reading', 'Sports'])

st.write("Your hobby is: ", hobby)

hobbies = st.multiselect("Hobbies: ",
                         ['Dancing', 'Reading', 'Sports'])

st.write("You selected", len(hobbies), 'hobbies')

st.button("Click me for no reason")

if st.button("About"):
    st.text("Welcome To GeeksForGeeks!!!")

name = st.text_input("Enter Your name", "Type Here ...")

if st.button('Submit'):
    result = name.title()
    st.success(result)