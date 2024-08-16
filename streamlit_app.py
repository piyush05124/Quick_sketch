from io import StringIO
import streamlit as st
import numpy as np
import pandas as pd
import time
from sketchModule import load_an_image,percentageResize,pencilSketch,convertto_watercolorsketch

def main():
    uploaded_files = st.file_uploader("Upload image")
    if uploaded_files is not None:
        # bytes_data = StringIO(uploaded_files.getvalue().decode("utf-8"))
        st.write("filename:", uploaded_files.name)
        # print(uploaded_files)
        x= load_an_image(uploaded_files)
        st.image(x,'Original image')
        h,w,ch = np.array(x).shape

        w_percent = percentageResize(w,80)
        h_percent = percentageResize(h,80)
       
        # action = st.button('pencil sketch')
        # if action :
        sigma_s = st.slider('chose sigma-s',1,150,step=1)
        sigma_r = st.slider('chose sigma-r',0.01,1.0,step=0.001)
        shade_factor = st.slider('chose shade-factor',0.01,1.0,step=0.001)
        # pencilSketch(inp_img,sigma_s,sigma_r,shade_factor)
        time.sleep(0.02)
        st.image(pencilSketch(np.array(x), sigma_s,sigma_r,shade_factor),'uploaded image')






if '__main__()':
    st.title(':blue[_Quick Sketch_]  :sunglasses:')
    main()
