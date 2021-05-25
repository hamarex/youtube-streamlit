import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

'start'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.01)



#st.title('streamlit GOGO ')

#st.write('DataFrame')

##df = pd.DataFrame(
#np.random.randn(100,2)/[50,50] + [35.69,139.70],
#columns=['lat','lon']
#)

#a + ar + a r^2 + \cdots + a r^{n-1} =
#''')

#st.line_chart(df)

#st.area_chart(df)

#st.bar_chart(df)

#st.map(df)

#st.write('display image')

#if st.checkbox('show Image'):
 #   img = Image.open('sam.jpeg')
 #   st.image(img,caption='DAREDA',use_column_width=True)


left_column, right_column = st.beta_columns(2)
button = left_column.button('右からむ')
if button:
    right_column.write('this is right!')

expander = st.beta_expander(' toiawase')
expander.write('toiawase wirte')


#text = st.text_input('what\'s you hobby ?')
#'you hobby is ', text

#condition = st.slider('you like?',0,100,50)
#'condition ? ', condition

##option = st.selectbox(
#    'you like this ?',
#    list(range(1,11))
#)

#'you like this,',option , ' cool!!'