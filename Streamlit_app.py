import streamlit as st
import pandas as pd
import pickle as pkl
def change_binary(x):
    if x=='Yes':
        return 1
    return 0
def read_file(filename):
    dst=[]
    with open(filename,'r') as f:
        for i in f:
            line = i.strip()
            if line and line != "None":
                dst.append(line)
    return dst
def open_pkl(filename):
    with open(filename,'rb') as file:
        return pkl.load(file)

st.title('🏠 House Prize Predictor 💸')

#Getting Inputs
posted_by=st.selectbox('Select the Category',['Owner','Dealer','Builder'])

under_cont=st.selectbox('Select Under Construction:',['Yes','No'])
under_cont=change_binary(under_cont)

rera=st.selectbox('Real-Est-Project',['Yes','No'])
rera=change_binary(rera)

bhk=st.slider('BHK:',min_value=1,max_value=25)

sqr_ft=st.number_input('Square Feet:')

rdt_to_move=st.selectbox('Are You Vacating:',['Yes','No'])
rdt_to_move=change_binary(rdt_to_move)

resale=st.selectbox('Resale :',['Yes','No'])
resale=change_binary(resale)

enc_dst = read_file('D:\PYTHON\my_project\encoded_district.txt')
address=st.selectbox('District :',enc_dst)

lat=st.number_input('Latitude :')

lon=st.number_input('Longitude :')

bhk_rk=st.selectbox('Property Type:',['BHK','RK'])
bhk_rk=1 if bhk_rk=='BHK' else 0

#Loading Model,Encoder,Scaler
model=open_pkl("D:\PYTHON\my_project\model.pkl")
scaler=open_pkl("D:\PYTHON\my_project\scaler.pkl")
enc=open_pkl("D:\PYTHON\my_project\enc.pkl")

df=pd.DataFrame(

{'POSTED_BY':[posted_by], 'UNDER_CONSTRUCTION':[under_cont], 'RERA':[rera], 'BHK_NO.':[bhk], 'BHK_OR_RK':[bhk_rk],
       'SQUARE_FT':[sqr_ft], 'READY_TO_MOVE':[rdt_to_move], 'RESALE':[resale], 'ADDRESS':[address], 'LONGITUDE':[lat],
       'LATITUDE':[lon]}
)

df=enc.transform(df)
df=scaler.transform(df)
pred=model.predict(df)
if st.button('Predict'):
    st.success(f"Predicted Prize: {pred}  (in lakhs)")