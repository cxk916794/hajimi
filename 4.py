import streamlit as st

st.set_page_config(page_title='马喽', page_icon='🐒')
images = [
    {
        'url':'https://tse3-mm.cn.bing.net/th/id/OIP-C.4qMuAASFxj6OYLWXN12v0AHaHF?o=7&cb=12rm=3&ucfimg=1&rs=1&pid=ImgDetMain&o=7&rm=3',
        'parm':'睡觉马喽'
    },
    {
        'url':'https://img.dancihu.com/pic/2024-01-13/1cacdea1-1cd1-bea5-05f0-dcb0c0af8ff0.png',
        'parm':'马喽去世'
    },
    {
        'url': 'https://ts1.tc.mm.bing.net/th/id/OIP-C.2xSpNXRmgIXDDNQsatvdkgHaHV?cb=12ucfimg=1&rs=1&pid=ImgDetMain&o=7&rm=3',
        'parm':'挑食马喽'
    }
  ]
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

def nextImg():
    st.session_state['ind'] = (st.session_state['ind']+1) % len(images)
def prevImg():
    st.session_state['ind'] = (st.session_state['ind']-1) % len(images)

st.image(images[st.session_state['ind']]['url'], caption=images[st.session_state['ind']]['parm'])
c1,c2 = st.columns(2)
with c1:
    st.button('上一张',on_click=prevImg,use_container_width=True)

with c2:
    st.button('下一张',on_click=nextImg,use_container_width=True)
