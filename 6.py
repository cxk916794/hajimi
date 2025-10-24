import streamlit as st
st.set_page_config(page_title='哈基米南北绿豆')

video_url = [
    {
        'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/86/72/32355387286/32355387286_qe1-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&oi=771356656&deadline=1761302198&trid=7316ed8795e942f3a51ca219dcd2847h&nbs=1&os=cosovbv&uipk=5&gen=playurlv3&og=hw&platform=html5&mid=0&upsig=cc59aa0a0ebb0a5d31ac3776adf7a64a&uparams=e,oi,deadline,trid,nbs,os,uipk,gen,og,platform,mid&bvc=vod&nettype=0&bw=625624&dl=0&f=h_0_0&agrr=1&buvid=&build=0&orderid=0,1',
        'title':'颗秒！',
        'episode':'1'
    },
    {
        'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/24/04/33281280424/33281280424-1-192.mp4?e=ig8euxZM2rNcNbRj7bdVhwdlhWTjhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&mid=0&deadline=1761302538&nbs=1&os=cosovbv&og=cos&oi=771356656&platform=html5&trid=342c937d1a9a44dab534758e1027a81h&uipk=5&gen=playurlv3&upsig=b65a64c11c508f2d4c90fe10bd22bc56&uparams=e,mid,deadline,nbs,os,og,oi,platform,trid,uipk,gen&bvc=vod&nettype=0&bw=1332116&buvid=&build=0&dl=0&f=h_0_0&agrr=1&orderid=0,1',
        'title':'剥蒜的情谊',
        'episode':'2'
    },
    {
        'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/44/95/32916769544/32916769544-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&platform=html5&os=cosovbv&oi=771356656&trid=bd823a962e974a33835c1caa510d7a3h&gen=playurlv3&og=cos&deadline=1761302666&mid=0&nbs=1&uipk=5&upsig=466fb24ebaa1d1bb69feb79f2dc4e65b&uparams=e,platform,os,oi,trid,gen,og,deadline,mid,nbs,uipk&bvc=vod&nettype=0&bw=575936&dl=0&f=h_0_0&agrr=1&buvid=&build=0&orderid=0,1',
        'title':'光头强和熊二对狙',
        'episode':'1'
    },
    
  ]
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

st.title(video_url[st.session_state['ind']]['title'] + '-第' + video_url[st.session_state['ind']]['episode'] + '集')
st.video(video_url[st.session_state['ind']]['url'])

c1,c2,c3 = st.columns(3)

def play(arg):
    st.session_state['ind'] = int(arg)
    
for i in range(len(video_url)):
    st.button('第' + str(i + 1) + '集',use_container_width=True,on_click=play,args=([i]))

