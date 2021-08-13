import streamlit as st
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier



def main():
	st.title("Track phone number location and provide service operator details")
	st.subheader("Build with python and streamlit")
	mobile_number=st.text_input("Enter phone No.:",type="password")
	if st.button("find"):
		ch_number=phonenumbers.parse(mobile_number,"CH")
		st.success("Country Name {}".format(geocoder.description_for_number(ch_number,"en")))
		services_operator=phonenumbers.parse(mobile_number,'RO')
		st.success("Service Operator:{}".format(carrier.name_for_number(services_operator,"en")))
           
if __name__=="__main__":
	main()