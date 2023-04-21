"""
Streamlit Cheat Sheet

App to summarise streamlit docs v1.8.0

There is also an accompanying png and pdf version

https://github.com/daniellewisDL/streamlit-cheat-sheet

v1.8.0 October 2021

Author:
    @daniellewisDL : https://github.com/daniellewisDL

Contributors:
    @arnaudmiribel : https://github.com/arnaudmiribel
    @akrolsmir : https://github.com/akrolsmir
    @nathancarter : https://github.com/nathancarter

"""

import streamlit as st
import pandas as pd
from pathlib import Path
import base64

st.title("streamlit play")

df = pd.read_csv("data/vgsales.csv")
st.line_chart(df)