import streamlit as st

st.title("Random Ass Website")

col1,col2=st.columns(2)

with col1:
    st.write('')






with col2:
    st.write("206 National Olympic Committee's (NOC) will compete at the Paris Games - each represents a particular country or region of the world. For each country/region, an identifying IOC code is recorded and also the name of the country/region and its population. Each NOC")

st.header('Courses Added')
st.subheader('Data Science')
st.subheader("DSA")


# st.subheader('pyrhon')
# st.subheader('sql')

# st.header("Added a new feature")


st.caption('Hello')

st.sidebar.title("Menu")
st.sidebar.markdown("""
- Home
- About
- Contact
- Career
- Login
""") 

st.sidebar.selectbox('Selet One',['teacher','student'])

st.sidebar.button("Select")