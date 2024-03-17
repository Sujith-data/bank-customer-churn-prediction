import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

# Define the Streamlit UI
def main():
    st.title('Bank Customer Churn')

    # Add UI components for user input
    age = st.number_input('Enter customer age:', min_value=18, max_value=100, value=30)
    gender = st.selectbox('Select customer gender:', ['Male', 'Female'])
    location = st.selectbox('Select customer location:', ['France', 'Germany', 'Spain'])
    tenure = st.number_input('Enter customer tenure (in years):', min_value=0, max_value=50, value=5)
    estimated_salary = st.number_input('Enter customer estimated salary:', min_value=0.0, value=300000.0)
    balance = st.number_input('Enter customer balance:', min_value=0.0, value=0.0)
    credit_score = st.number_input('Enter customer credit score:', min_value=300, max_value=850, value=700)
    num_of_products = st.number_input('Enter number of products:', min_value=1, value=1)
    is_active_member = st.radio('Is the customer an active member?', ['Yes', 'No'])

    # Once you have collected the necessary user inputs, use the model to make predictions
    if st.button('Predict'):
        # Perform any necessary data preprocessing based on user inputs
        gender_encoded = 1 if gender == 'Female' else 0
        location_encoded = {'France': 0, 'Germany': 1, 'Spain': 2}[location]
        is_active_member_encoded = 1 if is_active_member == 'Yes' else 0

        # Prepare input data for prediction
        input_data = [[age, gender_encoded, location_encoded, tenure, estimated_salary, balance, credit_score, num_of_products, is_active_member_encoded]]

        # Use the model to make predictions
        prediction = model.predict(input_data)

        # Display the prediction result
        st.write('Prediction:', prediction)

# Call the main function to run the Streamlit app
if __name__ == '__main__':
    main()
