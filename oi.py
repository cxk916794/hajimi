import streamlit as st

st.set_page_config(page_title='哈基米音乐', page_icon='🐒')
music = [
    {
        'url':'https://music.163.com/song/media/outer/url?id=2752844219.mp3',
        'name':'弥渡山歌（哈基米）',
        'photo':'https://ts4.tc.mm.bing.net/th/id/OIP-C.vEezsGpGrlM9ygxM3l9FpAAAAA?cb=ucfimgc2&pid=ImgDet&w=354&h=325&rs=1&o=7&rm=3',
        'author':'换挡拨片'
    },
    {
        'url':'https://music.163.com/song/media/outer/url?id=2643250369.mp3',
        'name':'Normal No More(哈基米)',
        'photo':'https://ts3.tc.mm.bing.net/th/id/OIP-C.7qcNa1OiBGDgZCLzV4iE9QAAAA?cb=ucfimgc2&rs=1&pid=ImgDetMain&o=7&rm=3',
        'author':'还我神ID'
    },
    {
        'url':'https://music.163.com/song/media/outer/url?id=2728770650.mp3',
        'name':'Move Your Body(哈基米)',
        'photo':'https://img.hefeirencai.cn/uploads/body_img/2025-04-29/20250429091653152516.jpg',
        'author':'DJ迈卡'
    },
    
  ]
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

def nextImg():
    st.session_state['ind'] = (st.session_state['ind']+1) % len(music)
def prevImg():
    st.session_state['ind'] = (st.session_state['ind']-1) % len(music)

a1,a2 = st.columns([1,2])
with a1:
    st.image(music[st.session_state['ind']]['photo'])
with a2:
    st.title(music[st.session_state['ind']]['name'])
    st.audio(music[st.session_state['ind']]['url'],autoplay=True)
    st.subheader(music[st.session_state['ind']]['author'])
    
c1,c2 = st.columns(2)

with c1:
    st.button('上一首',on_click=prevImg,use_container_width=True)

with c2:
    st.button('下一首',on_click=nextImg,use_container_width=True)
