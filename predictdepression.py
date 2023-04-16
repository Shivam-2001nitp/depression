import numpy as np
import pickle
import streamlit as st
import streamlit.components.v1 as components

# loading the saved model
loaded_model = pickle.load(open("depression_model.sav", 'rb'))


# creating a function for Prediction

def depression_model(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'You do not have Depression Symptoms'
    elif (prediction[0] == 1):
        return 'You have mild depression symptoms'
    else:
      return 'You have moderate depression symptoms'
  
    
  
def main():
    
    
    # giving a title
    st.title('Depression Prediction Web App')
    
    # getting the input data from the user
    
    
    gender = st.text_input('gender',placeholder="1-->female 2-->male")
    age = st.text_input('age',placeholder="Enter Your Age")
    afftype = st.text_input('afftype',placeholder="1--> bipolar II    2--> unipolar   3--> bipolar I")   
    melanch = st.text_input('melanch',placeholder="1--> sad   2--> Not sad")
    inpatient = st.text_input('inpatient', placeholder="1-->inpatient   2-->outpatient")
    marriage = st.text_input('marriage',placeholder="1--> married   2--> single")
    work = st.text_input('work',placeholder="1-->working   2--unemployed")
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Depression Test Result'):
      depression_prediction = depression_model([gender, age, afftype, melanch, inpatient, marriage, work])
      st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()