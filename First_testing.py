# prompt: can you help me built website using python , use streamlit,I want website for my clinic and should have clinic name OM Vardhan Clinic, should have clinic details like Clinic time, day , should have doctor name Dr Santosh Kumari Genral Physician should have Doctor Image, should have clinic address Dwarka Sector 8 Bagdola, should have oppointement booking option, should have email id omvardhanclinic@gmail.com

import streamlit as st
from PIL import Image

# Set page title
st.set_page_config(page_title="OM VARDHAN CLINIC")

# Clinic Information
st.title("OM Vardhan Clinic")

# Doctor Image
image = Image.open("dr.jpeg")  # Replace "doctor_image.jpg" with your image file
st.image(image, caption="Dr. Santosh Kumari", use_column_width=True)

# Doctor Details
st.header("Dr. Santosh Kumari")
st.write("General Physician(MD)- provides comprehensive, non-surgical healthcare, often serving as the first point of contact for patients seeking medical advice, diagnosing and treating a wide range of illnesses, and coordinating care, including referrals to specialists if needed. ")

# Clinic Timings
st.subheader("Clinic Timings")
st.write("Monday - Sunday: 07:00 PM - 09:00 PM")
st.write("Wednesday: Closed")


# Clinic Address
st.subheader("Clinic Address")
st.write("D Block, D110 to D117 block, near Shri Radha Krishna Mandir, Bagdola, Sector 8 Dwarka, Dwarka, New Delhi, Delhi, 110077")


# Appointment Booking
st.subheader("Book an Appointment")
appointment_date = st.date_input("Select Date")
appointment_time = st.time_input("Select Time")

if st.button("Book Appointment"):
    st.success("Your appointment has been booked successfully!")

# Contact Information
st.subheader("Contact Us")
st.write("Email: omvardhanclinic@gmail.com")
st.write("Contact: 9643552031/7838969292")
