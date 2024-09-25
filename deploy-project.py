import pandas as pd
import streamlit as st
import pickle
from pickle import load

b1,b2,b3 = st.columns(3,gap='large')

with b2:
    st.title('BANKRUPTANCY')


st.subheader('Parameter input', divider=True)

c1,c2 = st.columns(2)

with c1:

#model =pickle.load(open("C:/Users/Nitro V 15\Desktop/excelr-project1/Bankruptancy.pkl"))
    def input_feature():


        financial_flexibility = st.radio('financial_flexibility',[0.0,0.5,1.0])
        credibility = st.radio('credibility',[0.0,0.5,1.0])
        competitiveness =st.radio('competitiveness',[0.0,0.5,1.0])
        operating_risk=st.radio('operating risk',[0.0,0.5,1.0])

        data = {
            'financial_flexibility':financial_flexibility,
            'credibility':credibility,  
            'competitiveness' :competitiveness,
            "operating_risk":operating_risk
        }
        feature = pd.DataFrame(data,index=[0])
        return feature

    df = input_feature()


model =load(open("C:/Users/Nitro V 15/Desktop/excelr-project1/New folder/finalpickl/Bankruptancy.pkl",'rb'))
pred = model.predict(df)
pred_prob=model.predict_proba(df)

with c2:
    st.subheader('Prediction result')
    st.success('NON BANKRUPTANCY' if pred[0]==0 else 'BANKRUPTANCY')
    st.subheader('Prediction Probability')
    st.write("0 - NON BANCKRUPTACY")
    st.write("1 - BANKRUPTACY")
    st.write(pred_prob)