import streamlit as st
st.title("Cust_Segmentation")
import numpy as np
from tensorflow.keras.models import load_model 
model_path= 'model.h5'
model= load_model(model_path)
def predicted_value(Age,Edu,Years,Income,Card,Other,DebtIncomeRatio):
    result= np.array([[Age,Edu,Years,Income,Card,Other, DebtIncomeRatio]])
    prediction= model.predict(result)
    return prediction
Age = st.slider("Age", min_value=1, max_value=40)
Edu = st.slider("Edu", min_value=1, max_value=40)
Years = st.slider("Years", min_value=1, max_value=40)
Income = st.slider("Income", min_value=1, max_value=400)
Card = st.slider("Card", min_value=1, max_value=40)
Other = st.slider("Other", min_value=1, max_value=40)
DebtIncomeRatio = st.slider("DebtIncomeRatio", min_value=1, max_value=40)
if st.button("Predict"):
    cust_result = predicted_value(Age, Edu, Years, Income, Card, Other, DebtIncomeRatio)
    final = cust_result[0][0]
    
    # Display the result in the Streamlit app
    st.write(f"The predicted value is: {final}")
    
    if final > 0.5:
        st.write("Result is 1")
    else:
        st.write("Result is 0")


