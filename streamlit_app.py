import streamlit as st
import time as t

st.title("Welcome to hell")
st.header("Hi Boss")
st.subheader("Linear Regression")
st.info("The information for the user")
st.warning("The warning You want ti=o give to the user")
st.write("The Body you want to show in the page")

st.error("Wrong Passward")
st.success("Correct Pasword")

# Markdown
st.markdown("# Kaido")
st.markdown("## Roger")
st.markdown(":dragon:")

st.text("King of pirates")
st.caption("Kizokoni naru otuguda")

# Widgets

st.checkbox("Roronova")
st.button("zoro")
st.radio("What is his designation ",["Cook","Navigator","Swardsman"])
st.selectbox("What is his position in the team",["Captain","Vice Captain","Member"])

st.multiselect("Select Other Members",["Sanji","Kid","Garp","Chopper"])

st.select_slider("Zoro Swardsman Skills",["Bad","moderate","God","Excellent","Solo"])
st.slider("Rate his skills",0,100)

st.number_input("pick a number", 0, 10)
st.text_input("Enter the email")
st.date_input("Selecting the Date")
st.time_input("What is the timing for meeting")

st.text_area("Enter your view on the Zoro Swardsmanship")
st.file_uploader("Upload your drawings of Zoro")

with st.spinner("Just wait"):
    t.sleep(3)
    st.text("Onigiri")

st.sidebar.title("One Picece")
st.sidebar.text_input("Enter your email")
st.sidebar.text_input("Passward")
st.sidebar.button("Submit")