import streamlit as st
import pickle
import pandas as pd


def load_model():
    with open('cancer_model.sav', 'rb') as file:
        loaded_model = pickle.load(file)
    return loaded_model

Model = load_model()

def show_predict_page():
    st.title("Cancer Predictor")

    st.write("""we need some information""")

    
    Clump_Thickness = Cell_Size_Uniformity = Cell_Shape_Uniformity = Marginal_Adhesion = Single_Epi_Cell_Size = Bare_Nuclei = Bland_Chromatin = Normal_Nucleoli = Mitoses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    e1 = st.select_slider('Clump Thickness', Clump_Thickness, 3)
    e2 = st.select_slider('Cell Size Uniformity', Cell_Size_Uniformity)
    e3 = st.select_slider('Cell Shape Uniformity', Cell_Shape_Uniformity)
    e4 = st.select_slider('Marginal Adhesion', Marginal_Adhesion)
    e5 = st.select_slider('Single Epi Cell Size', Single_Epi_Cell_Size)
    e6 = st.select_slider('Bare Nuclei', Bare_Nuclei)
    e7 = st.select_slider('Bland Chromatin', Bland_Chromatin)
    e8 = st.select_slider('Normal Nucleoli', Normal_Nucleoli)
    e9 = st.select_slider('Mitoses', Mitoses)
    pred = st.button('Predict')
    if pred:
        data = [e1, e2, e3, e4, e5, e6, e7, e8, e9]
        x=['Clump_Thickness', 'Cell_Size_Uniformity', 'Cell_Shape_Uniformity', 'Marginal_Adhesion', 'Single_Epi_Cell_Size', 'Bare_Nuclei', 'Bland_Chromatin', 'Normal_Nucleoli', 'Mitoses']
        new_person = pd.DataFrame([data], columns=x)
        prediction = Model.predict(new_person)
        if prediction == 0:
            st.subheader('Paitent doesnot have Cancer')
            st.text('The Tumor may be Benign')
        else:
            st.subheader('Paitent has Cancer')
            st.text('The Tumor may be Malignant')

