import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    layout="wide",
    page_title = 'Campaign Prediction',
    page_icon = '🔮'
)
with open("styles.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
# import model
model = joblib.load('Model.pkl')
# import columns name
columns = joblib.load('columns.pkl')
# import encoding map 
encoder = joblib.load('Encoder_map.pkl')


def prediction(job,marital,education,housing, loan,contact,day_of_week,duration,campaign,pdays,emp,age_catigories):
    df = pd.DataFrame(columns = columns)
    df.at[0,'job'] = job
    df.at[0,'marital'] = marital
    df.at[0,'education'] = education
    df.at[0,'housing'] = housing
    df.at[0,'loan'] = loan
    df.at[0,'contact'] = contact
    df.at[0,'day_of_week'] = day_of_week
    df.at[0,'duration'] = duration 
    df.at[0,'campaign'] = campaign
    df.at[0,'pdays'] = pdays
    df.at[0,'emp.var.rate'] = emp
    df.at[0,'age_catigories'] = age_catigories
    for key in ['job','marital','education','housing','loan','contact','day_of_week','age_catigories']:
        df[key] = df[key].map(encoder[key])
    
    res = model.predict(df)
    return res[0]
    

st.title("Pridect if the client will subscribe a term deposit")
col1 , col2 , col3 = st.columns([1,0.25 ,1])
with col1:
    job = st.selectbox("job type" ,encoder['job'].keys() )
with col3 :
    marital = st.selectbox("marital status" ,encoder['marital'].keys() )
col4 , col5 , col6 = st.columns([1,0.25,1])
with col4 :
    education = st.selectbox("education degree" ,encoder['education'].keys() )
with col6 :
    housing = st.selectbox("housing loan" , ['yes' , 'no'])
col7 , col8 , col9 = st.columns([1,0.25 , 1])
with col7 :
    loan = st.selectbox("loan" ,['no', 'yes'] )
with col9 :
    contact = st.selectbox('type of contact',encoder['contact'].keys())
col10 , col11 , col12 = st.columns([1,0.25,1])
with col10 :
    day_of_week = st.selectbox('select day of call' , encoder['day_of_week'].keys())
with col12 :
    st.subheader(' if age < 18 select Teenagers / age < 30: select Youth / age < 45 select Young Adultsel / age < 65 select Adults / age > 65 select Elderly')
    age_catigories = st.selectbox('select age catigory', encoder['age_catigories'].keys()) 
col13 , col14 , col15 = st.columns([1,0.25,1])
with col13 :
    campaign = st.slider("number of call during campign" ,min_value=1,max_value=45,step = 1 , value = 1 )
with col15 :
    emp = st.slider("employment variation rate" ,min_value= -4.0,max_value=2.0,step = 0.1 , value =-1.1 )
col16 , col17 , col18 = st.columns([1,0.25,1])
with col16 :
    duration =  st.slider("duration of call" ,min_value=0,max_value=70,step = 1 , value = 1 )
with col18 :
    pdays = st.selectbox("number of days from the last call, " ,[0,1,2])
    st.subheader('NOTE : 0 means not contacted before, 1 means contacted one day ago, and 2 means contacted two or more days ago.')

if st.button("Predict"):
    result = prediction(job,marital,education,housing, loan,contact,day_of_week,duration,campaign,pdays,emp,age_catigories)
    res_list = ["no" , "yes"]
    st.text(res_list[result])
    
