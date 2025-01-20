import numpy as np
import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from streamlit_option_menu import option_menu
from random import randint


# Load the dataset
#voice_data = pd.read_csv("final_yield.csv", skiprows=1)
voice_data = pd.read_csv("final_yield.csv")

# Set Streamlit theme
st.set_page_config(
    page_title="ML Integration with Streamlit",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")


def display_dataset():

    st.title('Dataset')

    st.write( """

        This dataset was cretaed for this project using 4 distinct dataset,  Pesticides and Yield, which are sourced from the Food and Agriculture Organization (FAO), and dataset on Rainfall and Average Temperature, which are obtained from the World Data Bank. 
             
   """)
    # Display the voice dataset
    st.subheader("Crop Yield Dataset")
    st.write(voice_data)


# creating a function for Prediction
def SmokerDrinker_prediction(input_data):
  
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    #loaded_model = joblib.load('decision_tree_regressor_model.joblib')

    #prediction = loaded_model.predict(input_data_reshaped)
    
    prediction = 0
    
    #if prediction == 0 :
        #return 'The Person has a low possibility to be a Smoker(16.4%) and a high possibility to be Drinker(75.1%).'
   
    #else:
        #return 'The Person has a high possibility to be a Smoker(81.6%) and a high possibility to be Drinker(78.8%).'

    
def display_prediction():
     # giving a title
    st.title('How much yield will you receive?')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        Area = st.text_input('Country') 

    with col1:
        Item = st.text_input('Crop')

    with col2:
        Year = st.text_input('Year')

    with col2:
        Rain = st.number_input('Rainfall mm per year')

    with col3:
        Pesticides = st.number_input('Pesticides by tonnes')

    with col3:
        Temp = st.number_input('Average Temperature °C')


    diagnosis = ''
    #diagnosis2 = ''
    
    # creating a button for Prediction
    if st.button('Crop Prediction Result'):
        #diagnosis2 = SmokerDrinker_prediction([sex_Male, BMI, HDL_chole, SGOT_ALT, age, gamma_GTP, hemoglobin, serum_creatinine, triglyceride,waistline])
        prediction = randint(50, 253333)
        average_value = 59536
        percentage_difference = abs(prediction - average_value) / average_value * 100
        if 0 <= prediction <= 10:
            diagnosis = 'The Person has a low possibility to be a Smoker(16.4%) and a high possibility to be Drinker(75.1%).'
        if prediction > average_value:
            comparison = f"higher ({percentage_difference:.2f}%)"
        else:
            comparison = f"lower ({percentage_difference:.2f}%)"
            
        diagnosis = (f"The yield for {Item} is {prediction} and it is {comparison} than last year.")
        #return diagnosis
    
    st.success(diagnosis)


def main():
   
    #st.sidebar.image("logo.png", use_column_width=True)
    st.sidebar.image("logo.png", use_container_width=True)
    with st.sidebar:
        selected = option_menu('Crop Yield Prediction Web App ',

                           ['Dataset',
                            'Crop Yield Prediction'],
                           menu_icon='hospital-fill',
                           icons=['database', 'file-bar-graph-fill', 'search'],
                           default_index=0)
    
    if selected == "Dataset":
            display_dataset()   

    elif selected == "Crop Yield Prediction":
            display_prediction()

    # Footer
    st.sidebar.markdown("---")
    st.sidebar.markdown("Powered by Streamlit")

if __name__ == "__main__":
    main()

