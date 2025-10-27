import streamlit as st
import pandas as pd
from io import StringIO
from io import BytesIO
from datetime import datetime, time
st.set_page_config(page_title="个人简历生成器", page_icon="", layout="wide")
st.title('个人简历生成器')
c1, c2 = st.columns([1,2])
with c1:
    st.subheader('特战干员资料')
    st.markdown('***')
    def my_format_func(option):
        return f'{option}'
    name = st.text_input('姓名', autocomplete='name')
    size = st.radio(
    '性别',
    ['男', '女', '沃尔玛购物袋'],
    horizontal=True,
    label_visibility='hidden',)
    learn = st.selectbox('国籍：',['英国', '欧洲', '日本','俄罗斯','哈基米国'], format_func=my_format_func, index=2)
    languages = st.multiselect('精通语言：',['俄语', '英语', '法语','日语','哈基米语','火星文'],format_func=my_format_func)
    job = st.text_input('应聘职位', autocomplete='job')
    tl = st.text_input('干员职业', autocomplete='tl')
    email = st.text_input('邮箱', autocomplete='email') 
    age = st.number_input("年龄", min_value=1, max_value=130, value=10)
    date = st.date_input("生日", value=None)
    w3 = st.time_input("活跃时间段", datetime(2019, 7, 6, 21, 15))
    age = st.slider('工龄', 0, 50)
    values = st.slider(
    '期望薪资',
    0, 100000,(10000, 20000))
    t5 = st.text_area(label='个人简介：', placeholder='请简单描述自己')
    uploaded_file = st.file_uploader("上传个人照片", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        
        
    
    
with c2:
    st.subheader('实时简历预览')
    st.markdown('***')
    a1, a2, a3 = st.columns(3)
    with a1:
        if uploaded_file is not None:
            bytes_data = uploaded_file.getvalue()
            st.image(bytes_data, caption="本人照片", width=250)
        
    with a2:
        st.title(name)
        st.write('**国籍**:',learn)
        st.write(f'**性别**:{size}')
        st.write('**邮箱**:', email)
        st.write('**干员职业**:', tl)
        st.write('**年龄**:', age)
    with a3:
        st.write('**应聘职位**:', job)
        st.write("**生日**:", date)
        st.write("**活跃时间段**:", w3)
        st.write('**期望薪资**:', values)
        st.write('**精通语言**:', languages)
        st.write("**工龄**: ", age, '年')
        
    st.markdown('***')
    st.title('**个人简介**')
    st.write(t5)
