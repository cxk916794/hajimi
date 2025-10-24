import streamlit as st

st.set_page_config(page_title='简易音乐播放器', page_icon='🎵', layout='wide')

st.header('🎵 简易音乐播放器', divider='rainbow')
st.write("""
使用streamlit制作的简易音乐播放器，收录了陈卓璇的几首精选歌曲。
你可以通过下方的按钮切换歌曲，欣赏优美的旋律。所有音乐资源均来自网易云音乐。
""")
music = [
    {
        'url': 'https://music.163.com/song/media/outer/url?id=2654783608.mp3',
        'name': '<<海与天之间>>',
        'singer': '陈卓璇',
        'photo': 'https://p2.music.126.net/dHRiObdSjpAEidbzur6g9A==/109951170239854759.jpg',
        'producer': '颜小健@jyken',
        'lyricist': '张鹏鹏',  
        'composer': '颜小健',  
        'desc': '这首歌曲旋律轻快，歌词描绘了对自由与远方的向往，展现了独特的音乐风格。'
    },
    {
        'url': 'https://music.163.com/song/media/outer/url?id=2722153067.mp3',
        'name': '<<深海之息>>',
        'singer': '陈卓璇',
        'photo': 'https://p1.music.126.net/oFCXvJMRkEtZhTdGfs3QmA==/109951171835214529.jpg',
        'producer': '陈卓璇',
        'lyricist': '陈卓璇',  
        'composer': '陈卓璇',  
        'desc': '歌曲以深海为意象，表达了内心深处的情感波动，身处极度深沉的深海中向上的自我救赎。'
    },
    {
        'url': 'https://music.163.com/song/media/outer/url?id=2738035652.mp3',
        'name': '<<昨夜风今宵月>>',
        'singer': '陈卓璇',
        'photo': 'https://p1.music.126.net/cJybH1TkQM27f7XWsJNqkw==/109951171900496609.jpg',
        'producer': '代诗琪/曾吴秋杰',
        'lyricist': '有礼',  
        'composer': '代诗琪',  
        'desc': '古风韵味十足的一首歌曲，将传统意境与现代旋律结合，画面感强烈。'
    }
]

if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

def next_song():
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(music)

def prev_song():
    st.session_state['ind'] = (st.session_state['ind'] - 1) % len(music)

col1, col2 = st.columns([1, 2], gap='large')

with col1:
    st.image(
        music[st.session_state['ind']]['photo'],
        use_container_width=True,
        caption=f"当前播放: {music[st.session_state['ind']]['name']}"
    )

with col2:
    st.subheader(music[st.session_state['ind']]['name'], divider='blue')
    st.write(f"🎤 歌手: {music[st.session_state['ind']]['singer']}")
    st.write(f"✏️ 作词: {music[st.session_state['ind']]['lyricist']}")  
    st.write(f"🎹 作曲: {music[st.session_state['ind']]['composer']}")  
    st.write(f"🎧 制作人: {music[st.session_state['ind']]['producer']}")
    st.write(f"📝 歌曲简介: {music[st.session_state['ind']]['desc']}")
    
    st.audio(
        music[st.session_state['ind']]['url'],
        format='audio/mp3',
        autoplay=True
    )

btn_col1, btn_col2 = st.columns(2, gap='small')

with btn_col1:
    st.button(
        '◀️ 上一首',
        on_click=prev_song,
        use_container_width=True
    )

with btn_col2:
    st.button(
        '下一首 ▶️',
        on_click=next_song,
        use_container_width=True
    )

st.caption('---')
st.caption('播放器仅用于学习交流，所有音乐版权归原作者所有')
