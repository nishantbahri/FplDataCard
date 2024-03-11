import streamlit as st

class Helper:

    @staticmethod
    def validate_api_input(input_text):
        try:
            # Attempt to convert the input to an integer
            int_value = int(input_text)

            return int_value  # Return the integer value if successful
        except ValueError:
            # Handle the case where the input is not a valid integer
            st.error("Please enter a valid integer as team/league id.")  # Display an error message
            return None  # Return None to indicate an invalid input