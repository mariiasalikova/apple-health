import streamlit as st
import pandas as pd
import re
from lxml import etree


#OTHER_KEYS = ["type", "sourceName", "unit"]
ALL_KEYS = ["startDate", "value", "type"]
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    tree = etree.parse(uploaded_file)
    root = tree.getroot()
    records = tree.xpath("//Record")
    # Get all records where as source the apple watch is
    df = pd.DataFrame([{key: r.get(key) for key in ALL_KEYS} for r in records if 'Apple' in r.attrib['sourceName']])

    df_heart = df.query('type == "HKQuantityTypeIdentifierHeartRate"')
    st.line_chart(df_heart, x="startDate")