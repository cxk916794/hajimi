import streamlit as st
st.title("哈基米哦南北绿豆🐱")
st.header("阿西嘎哈椰果奶龙🐱")
st.subheader("哈基米哦哦🔞")
st.text("欧马吉力曼波🐱")
st.subheader("Python代码块")
python_code = '''def hello():
    print("头甲枪🔫胸挂背包 花来💐！")
'''
st.code(python_code, language=None)
st.caption('捷风：颗秒！')
st.caption('<i>不死鸟：饿啊</i>', unsafe_allow_html=True)
st.caption('<center>捷风：咦嘻嘻嘻</center>',unsafe_allow_html=True)
st.markdown(':red[尚博乐：他们走不了了！]')
st.markdown('*捷风：布豪，是炸鱼哥*')
st.markdown('**尚博乐：跪下**')
st.markdown(':green[捷风：饿啊]')
import streamlit as st
# 页面配置：科幻深色风格
st.set_page_config(page_title="蜂医-数字档案", layout="wide", initial_sidebar_state="collapsed")
# 自定义CSS实现科幻风格
st.markdown(
    """
    
    """,
    unsafe_allow_html=True
)
# 标题
st.title("三角洲干员 - 蜂医·数字档案")
# Header
st.header("罗伊*斯米 基础信息")
image_path = "D:\\哈基蜂.jpg"  # 替换为你D盘中实际的JPG图片路径，注意反斜杠要转义或用正斜杠
st.image(image_path, caption="D盘JPG图片展示", use_column_width=True)
# Text
st.text("代号：蜂医")
st.text("编号：DELTA-007")
st.text("注册时间：2145-07-12 | 状态：**现役** ✅")
st.text("当前健康度：98% | 战斗评级：**S+**")
# Metric 技能矩阵
st.header("🧬 技能矩阵")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("激素枪", "95%", "↑5%")
with col2:
    st.metric("蜂巢烟幕", "92%", "↑2%")
with col3:
    st.metric("蜂巢科技烟雾弹", "88%", "↓1%")
# 进度条
st.header("💊 药剂研发进度")
st.progress(75, text="蜂针剂·改良版")
# Table 任务日志
st.header("📜 任务日志")
task_data = {
    "日期": ["2145-09-01", "2145-09-15", "2145-10-05"],
    "任务": ["战区伤员急救", "新型病毒溯源", "敌方据点医疗设施破坏"],
    "状态": ["✅ 完成", "🔄 进行中", "✅ 完成"],
    "评级": ["★★★★☆", "★★★★★", "★★★☆☆"]
}
st.table(task_data)
# Code 最新作战记录代码片段
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
# Markdown 系统提示
st.markdown("---")
st.markdown("> 下一个任务将在**2145-10-10 08:00**开启，请提前准备「蜂群医疗单元」。\n> *系统状态：全链路稳定 | 档案已加密*")
