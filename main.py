from cgitb import text
from imp import NullImporter
from turtle import color
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')
st.write('Interative Widgets')

st.write('プログラスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

import time
for i in range(100):
    latest_iteration.text(f'Loading {i+1}')
    bar.progress(i+1)
    time.sleep(0.001)

# left_clomun, right_column = st.columns(2)

# button = left_clomun.button('右カラムに文字を表示')
# if button:
#     right_column.write('ここは右カラムです')

# expander1 = st.expander('問い合わせ1')
# expander1.write('問い合わせ1の回答')
# expander2 = st.expander('問い合わせ2')
# expander2.write('問い合わせ2の回答')
# expander3 = st.expander('問い合わせ3')
# expander3.write('問い合わせ3の回答')

expander1 = st.expander('問い合わせ1')
t = expander1.text_input('入力してください')
expander1.write(t)

expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')



# option = st.text_input('あなたの趣味を教えて下さい')
# 'あなたの好きな趣味は', option, 'です。'

# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'コンディション：', condition


# if st.checkbox('Show Image'):
#     img = Image.open('Teams用.PNG')
#     st.image(img, caption='Shinjiro', use_column_width=True)
# else:
#     st.write('押してみてね！')

# number = list(range(1,10))
# option = st.selectbox(
#     'あなたが好きな数字を教えて下さい',
#     number
# )
#'あなたが好きな数字は、', option, 'です。'

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
#st.dataframe(df.style.highlight_max(axis=0, color='red'), width=300)

#st.map(df, zoom=None)

