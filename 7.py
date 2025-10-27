import streamlit as st

st.set_page_config(page_title="干员档案", page_icon="", layout="wide")

import streamlit as st

st.subheader('干员信息')
name = st.text_input('姓名', autocomplete='name')

st.text_input('所属国家')

st.text_input('兵种')

st.text_input('联系方式')

import streamlit as st
from datetime import datetime, timedelta

# value参数默认为None，初始状态为今天
date = st.date_input("出生日期", value=None)

def my_format_func(option):
    return f'选{option}'

st.write('性别')
# 设置标签为“hidden”
# 设置水平排列
lunch = st.radio(
    '你的性别是什么？',
    ['男', '女', '沃尔玛购物袋'],
    horizontal=True,
    label_visibility='hidden'
)

city = st.selectbox('学历：', ['幼儿园', '小学', '初中','高中','大学'], format_func=my_format_func, index=2)

city = st.selectbox('喜欢的食物：', ['扣肉拿铁', '爆辣冰淇淋', '哈基米南北绿豆','白丝乌鲁鲁'], format_func=my_format_func, index=2)

options_2 = st.multiselect(
    '擅长的技能',
    ['蜂巢烟幕', '蜂巢科技烟雾弹', '治疗激素枪', '高效救援', '乞讨'],
    max_selections=5)

import streamlit as st
from datetime import datetime, time

age = st.slider('作战时间', 0, 100)
st.write("以作战 ", age, '年')

start_color, end_color = st.select_slider(
    '期望薪资范围',
    options=['1', '5000', '10000', '15000', '20000', '25000', '30000'],
    value=('1', '15000'))
st.write('你期望的薪资介于', start_color, '和', end_color, '之间')

init_text = "罗伊出生于治安混乱的小镇，青少年时期曾陷入街头帮派活动，成年后参军并师从老军医学习急救技术。因战场救援表现突出获得进修机会，后加入特种部队支援群。其家庭由妻子和八岁女儿组成，所有收入均寄回家乡。"
st.text_area(label='个人简介：', value=init_text,
            height=200, max_chars=200)

w2 = st.time_input("活跃时间", time(2,00))
st.write("你选择时间2是:", w2)

import streamlit as st
import pandas as pd
from io import StringIO
st.header('上传个人照片')
uploaded_file = st.file_uploader("选择一个CSV文件")
if uploaded_file is not None:
    bytes_date = uploaded_file.getvalue()
    st.subheader('直接展示字节数据')
    st.write(bytes_data)
