# 统一导入所有需要的库（只导入一次）
import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO, BytesIO
from datetime import datetime, time

# 页面配置必须放在所有输出内容之前（重要！只能调用一次）
st.set_page_config(
    page_title="顶部栏", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 定义选项卡
st.title("选项卡")
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["数字档案", "美食数据", '相册', '音乐', '视频播放器', '个人简介生成器'])

# ==================== 第一个选项卡内容（tab1）====================
with tab1:
    st.title("哈基米哦南北绿豆🐱")
    st.header("阿西嘎哈椰果奶龙🐱")
    st.subheader("哈基米哦哦🔞")
    st.text("欧马吉力曼波🐱")
    
    st.subheader("Python代码块")
    python_code = '''def hello():
        print("头甲枪🔫胸挂背包 花来💐！")
    '''
    st.code(python_code, language="python")
    
    st.caption('捷风：颗秒！')
    st.caption('<i>不死鸟：饿啊</i>', unsafe_allow_html=True)
    st.caption('<center>捷风：咦嘻嘻嘻</center>', unsafe_allow_html=True)
    
    st.markdown(':red[尚博乐：他们走不了了！]')
    st.markdown('*捷风：布豪，是炸鱼哥*')
    st.markdown('**尚博乐：跪下**')
    st.markdown(':green[捷风：饿啊]')

    st.title("三角洲干员 - 蜂医·数字档案")
    st.header("罗伊*斯米 基础信息")
    
    image_path = "4f88299f4456bd303979e8770dc396ca0814641f.jpg"  # 替换为实际路径
    st.image(image_path, caption="图片展示", use_column_width=True)
    
    st.text("代号：蜂医")
    st.text("编号：DELTA-007")
    st.text("注册时间：2145-07-12 | 状态：**现役** ✅")
    st.text("当前健康度：98% | 战斗评级：**S+**")
    
    st.header("🧬 技能矩阵")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("激素枪", "95%", "↑5%")
    with col2:
        st.metric("蜂巢烟幕", "92%", "↑2%")
    with col3:
        st.metric("蜂巢科技烟雾弹", "88%", "↓1%")
    
    st.header("💊 药剂研发进度")
    st.progress(75, text="蜂针剂·改良版")
    
    st.header("📜 任务日志")
    task_data = {
        "日期": ["2145-09-01", "2145-09-15", "2145-10-05"],
        "任务": ["战区伤员急救", "新型病毒溯源", "敌方据点医疗设施破坏"],
        "状态": ["✅ 完成", "🔄 进行中", "✅ 完成"],
        "评级": ["★★★★☆", "★★★★★", "★★★☆☆"]
    }
    st.table(task_data)
    
    st.header("💻 最新作战记录代码片段")
    code = """
    def bee_medic_heal(target, emergency_level):
        if emergency_level > 8:
            use_super_venom("heal_mode")
            target.health += 50
            st.write("【蜂医】：极限生命维持已启动！")
        else:
            use_bee_needle("regenerate")
            target.health += 30
            st.write("【蜂医】：常规修复完成。")
        return target.health
    """
    st.code(code, language="python")
    
    st.markdown("---")
    st.markdown("> 下一个任务将在**2145-10-10 08:00**开启，请提前准备「蜂群医疗单元」。\n> *系统状态：全链路稳定 | 档案已加密*")


# ==================== 第二个选项卡内容（tab2）====================
with tab2:
    st.title("🍲桂林美食探索🥢")
    st.text("📷探索广西桂林最受欢迎的美食地点！选择你感兴趣的餐厅类型，查看评分和位置.")
    
    shops_data = {
        "店铺名称": ["阿秀米粉", "李记阳朔啤酒鱼老店", "蒋记王城糯米饭", "油茶故里", "椿记烧鹅"],
        "特色美食": ["桂林米粉🍜", "🍺阳朔啤酒鱼🐟", "传统糯米饭🍙", "恭城油茶🧉", "烧鹅🦢"],
        "人均消费":[5,60,10,30,40],
        "评分": [4.5, 4.7, 4.6, 4.7, 4.8],
        "地址": ["七星区建干路", "象山区南环路", "秀峰区秀峰街道", "七星区龙隐园", "象山区中山中路"],
        "纬度": [25.277666, 25.268197, 25.275264, 25.263762, 25.268743],
        "经度": [110.312878, 110.290799, 110.299844, 110.303532, 110.289686],
    }
    shops_df = pd.DataFrame(shops_data)
    
    months = [f"{i}月" for i in range(1, 13)]
    price_data = {
        "月份": months,
        "阿秀米粉": np.random.uniform(10, 20, 12),
        "李记阳朔啤酒鱼老店": np.random.uniform(80, 120, 12),
        "蒋记王城糯米饭": np.random.uniform(5, 10, 12),
        "油茶故里": np.random.uniform(15, 25, 12),
        "椿记烧鹅": np.random.uniform(30, 50, 12)
    }
    price_df = pd.DataFrame(price_data)
    price_df.set_index("月份", inplace=True)
    
    st.subheader("🚀桂林美食店铺信息")
    st.dataframe(shops_df)
    
    st.subheader("💰桂林美食店铺价格走势↗️↘️（12个月）")
    st.line_chart(price_df)
    
    st.subheader("⭐桂林美食店铺评分对比")
    st.bar_chart(shops_df.set_index("店铺名称")["评分"])
    
    sales_data = {
        "月份": months,
        "阿秀米粉": np.random.uniform(200, 300, 12),
        "李记阳朔啤酒鱼老店": np.random.uniform(100, 180, 12),
        "蒋记王城糯米饭": np.random.uniform(150, 250, 12),
        "油茶故里": np.random.uniform(80, 150, 12),
        "椿记烧鹅": np.random.uniform(60, 120, 12)
    }
    sales_df = pd.DataFrame(sales_data).set_index("月份")
    st.subheader("✈️桂林美食店铺销量走势（面积图）")
    st.area_chart(sales_df)
    
    map_data = {
        'latitude':[25.277666,25.268197,25.275264,25.263762,25.268743],
        'longitude':[110.312878,110.290799,110.299844,110.303532,110.289686]
    }
    st.map(pd.DataFrame(map_data))


# ==================== 第三个选项卡内容（tab3：相册）====================
with tab3:
    # 相册数据
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
    
    # 独立的session_state键
    if 'tab3_ind' not in st.session_state:
        st.session_state['tab3_ind'] = 0
    
    # 切换图片函数
    def nextImg():
        st.session_state['tab3_ind'] = (st.session_state['tab3_ind'] + 1) % len(images)
    def prevImg():
        st.session_state['tab3_ind'] = (st.session_state['tab3_ind'] - 1) % len(images)
    
    # 显示当前图片
    st.image(images[st.session_state['tab3_ind']]['url'], 
             caption=images[st.session_state['tab3_ind']]['parm'],
             use_column_width=True)
    
    # 切换按钮
    c1, c2 = st.columns(2)
    with c1:
        st.button('上一张', on_click=prevImg, use_container_width=True)
    with c2:
        st.button('下一张', on_click=nextImg, use_container_width=True)


# ==================== 第四个选项卡内容（tab4：音乐）====================
with tab4:
    # 音乐数据
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
    
    # 独立的session_state键
    if 'tab4_ind' not in st.session_state:
        st.session_state['tab4_ind'] = 0
    
    # 切换音乐函数
    def nextMusic():
        st.session_state['tab4_ind'] = (st.session_state['tab4_ind'] + 1) % len(music)
    def prevMusic():
        st.session_state['tab4_ind'] = (st.session_state['tab4_ind'] - 1) % len(music)
    
    # 显示音乐信息
    a1, a2 = st.columns([1, 2])
    with a1:
        st.image(music[st.session_state['tab4_ind']]['photo'], use_column_width=True)
    with a2:
        st.title(music[st.session_state['tab4_ind']]['name'])
        st.audio(music[st.session_state['tab4_ind']]['url'], autoplay=True)
        st.subheader(f"作者：{music[st.session_state['tab4_ind']]['author']}")
    
    # 切换按钮
    c1, c2 = st.columns(2)
    with c1:
        st.button('上一首', on_click=prevMusic, use_container_width=True)
    with c2:
        st.button('下一首', on_click=nextMusic, use_container_width=True)


# ==================== 第五个选项卡内容（tab5：视频播放器）====================
with tab5:
    # 视频数据
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
    
    # 独立的session_state键（避免与其他选项卡冲突）
    if 'tab5_ind' not in st.session_state:
        st.session_state['tab5_ind'] = 0
    
    # 显示当前视频信息
    st.title(f"{video_url[st.session_state['tab5_ind']]['title']}-第{video_url[st.session_state['tab5_ind']]['episode']}集")
    st.video(video_url[st.session_state['tab5_ind']]['url'])
    
    # 切换视频函数
    def play(arg):
        st.session_state['tab5_ind'] = int(arg)
    
    # 集数选择按钮（用列布局更整齐）
    cols = st.columns(len(video_url))
    for i, col in enumerate(cols):
        with col:
            st.button(f'第{i+1}集', use_container_width=True, on_click=play, args=([i]))


# ==================== 第六个选项卡内容（tab6：个人简介生成器）====================
with tab6:
    st.title('个人简历生成器')
    c1, c2 = st.columns([1, 2])
    
    with c1:
        st.subheader('特战干员资料')
        st.markdown('***')
        
        def my_format_func(option):
            return f'{option}'
        
        name = st.text_input('姓名', autocomplete='name')
        gender = st.radio(  # 变量名从size改为gender，更语义化
            '性别',
            ['男', '女', '沃尔玛购物袋'],
            horizontal=True,
            label_visibility='hidden',
        )
        nationality = st.selectbox(  # 变量名从learn改为nationality
            '国籍：',
            ['英国', '欧洲', '日本', '俄罗斯', '哈基米国'],
            format_func=my_format_func,
            index=2
        )
        languages = st.multiselect(
            '精通语言：',
            ['俄语', '英语', '法语', '日语', '哈基米语', '火星文'],
            format_func=my_format_func
        )
        job = st.text_input('应聘职位', autocomplete='job')
        occupation = st.text_input('干员职业', autocomplete='tl')  # 变量名从tl改为occupation
        email = st.text_input('邮箱', autocomplete='email') 
        age = st.number_input("年龄", min_value=1, max_value=130, value=10)  # 年龄（数字输入）
        birthday = st.date_input("生日", value=None)  # 变量名从date改为birthday
        active_time = st.time_input("活跃时间段", datetime(2019, 7, 6, 21, 15))  # 变量名从w3改为active_time
        work_age = st.slider('工龄', 0, 50)  # 工龄（滑块，避免与age冲突）
        salary_range = st.slider(  # 变量名从values改为salary_range
            '期望薪资',
            0, 100000, (10000, 20000)
        )
        intro = st.text_area(label='个人简介：', placeholder='请简单描述自己')  # 变量名从t5改为intro
        uploaded_file = st.file_uploader("上传个人照片", type=["jpg", "png", "jpeg"])
        
        if uploaded_file is not None:
            photo_bytes = uploaded_file.getvalue()  # 变量名从bytes_data改为photo_bytes
    
    with c2:
        st.subheader('实时简历预览')
        st.markdown('***')
        a1, a2, a3 = st.columns(3)
        
        with a1:
            if uploaded_file is not None:
                st.image(photo_bytes, caption="本人照片", width=250)
        
        with a2:
            st.title(name)
            st.write('**国籍**:', nationality)
            st.write(f'**性别**: {gender}')
            st.write('**邮箱**:', email)
            st.write('**干员职业**:', occupation)
            st.write('**年龄**:', age)
        
        with a3:
            st.write('**应聘职位**:', job)
            st.write("**生日**:", birthday)
            st.write("**活跃时间段**:", active_time)
            st.write('**期望薪资**:', salary_range)
            st.write('**精通语言**:', languages)
            st.write("**工龄**: ", work_age, '年')  # 显示工龄（滑块变量）
        
        st.markdown('***')
        st.title('**个人简介**')
        st.write(intro)

