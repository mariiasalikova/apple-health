import streamlit as st
import pandas as pd
import re
from lxml import etree

st.title(':rainbow-background[Apple health analyser] :heart:')
st.write('App for analyse data from your Apple devices! :sunglasses:')
#OTHER_KEYS = ["type", "sourceName", "unit"]
ALL_KEYS = ["startDate", "value", "type"]
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    tree = etree.parse(uploaded_file)
    root = tree.getroot()
    records = tree.xpath("//Record")
    # Get all records where as source the apple watch is
    #if 'Apple' in r.attrib['sourceName']
    df = pd.DataFrame([{key: r.get(key) for key in ALL_KEYS} for r in records])

    df_heart = df.query('type == "HKQuantityTypeIdentifierHeartRate"')
    
    df_heart['value'] = df_heart['value'].str.replace(',', '.')
    df_heart['value'] = pd.to_numeric(df_heart['value'])
    
    st.line_chart(df_heart, x="startDate", y="value")
    
    df_steps = df.query('type == "HKQuantityTypeIdentifierStepCount"')
    df_steps['value'] = df_steps['value'].str.replace(',', '.')
    df_steps['value'] = pd.to_numeric(df_steps['value'])
    
    st.line_chart(df_steps, x="startDate", y="value")