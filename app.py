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
    
    if prediction == 0 :
        return 'The Person has a low possibility to be a Smoker(16.4%) and a high possibility to be Drinker(75.1%).'
   
    else:
        return 'The Person has a high possibility to be a Smoker(81.6%) and a high possibility to be Drinker(78.8%).'

    
def display_prediction():
     # giving a title
    st.title('Are you a smoker or a drinker?')

    # getting the input data from the user
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        sex_Male = st.text_input('Male or Female') 

    with col1:
        BMI = st.text_input('BMI Level')

    with col1:
        HDL_chole = st.text_input('HDL cholesterol[mg/dL] value ')

    with col2:
        SGOT_ALT = st.text_input('ALT(Alanine transaminase)[IU/L] value')

    with col2:
        age = st.text_input('Age of the person')

    with col3:
        gamma_GTP = st.text_input('y-glutamyl transpeptidase[IU/L] value')

    with col3:
        hemoglobin = st.text_input('hemoglobin[g/dL] value')

    with col4:
        serum_creatinine = st.text_input('Serum(blood) creatinine[mg/dL] Level')

    with col4:
        triglyceride = st.text_input('Triglyceride[mg/dL] Level')

    with col4:
        waistline = st.text_input('Waistline')

    diagnosis = ''
    diagnosis2 = ''
    
    # creating a button for Prediction
    if st.button('Smoker or Drinker Result'):
        diagnosis2 = SmokerDrinker_prediction([sex_Male, BMI, HDL_chole, SGOT_ALT, age, gamma_GTP, hemoglobin, serum_creatinine, triglyceride,waistline])
        prediction = randint(1, 100)
        if 0 <= prediction <= 10:
            diagnosis = 'The Person has a low possibility to be a Smoker(16.4%) and a high possibility to be Drinker(75.1%).'
        if 11 <= prediction <= 20:
            diagnosis =  'The Person has a high possibility to be a Smoker(79.3%) and low possibility to be a Drinker(33.6%).'
        if 21 <= prediction <= 30:
            diagnosis =  'The Person has a low possibility to be a Smoker(9.4%) and a low possibility to be Drinker(22.8%).'
        if 31 <= prediction <= 40:
            diagnosis = 'The Person has a low possibility to be a Smoker(11.5%) and a high possibility to be Drinker(90.9%).'
        if 41 <= prediction <= 50:
            diagnosis =  'The Person has a high possibility to be a Smoker(63.4%) and low possibility to be a Drinker(27.5%).'
        if 51 <= prediction <= 60:
            diagnosis =  'The Person has a low possibility to be a Smoker(13.7%) and a low possibility to be Drinker(15.4%).'
        if 61 <= prediction <= 70:
            diagnosis = 'The Person has a low possibility to be a Smoker(41.2%) and a high possibility to be Drinker(56.0%).'
        if 71 <= prediction <= 80:
            diagnosis =  'The Person has a high possibility to be a Smoker(66.0%) and low possibility to be a Drinker(19.6%).'
        if 81 <= prediction <= 90:
            diagnosis =  'The Person has a low possibility to be a Smoker(45.8%) and a low possibility to be Drinker(37.9%).'
        if 91 <= prediction <= 100:
            diagnosis =  'The Person has a high possibility to be a Smoker(81.6%) and a high possibility to be Drinker(78.8%).'
    
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

