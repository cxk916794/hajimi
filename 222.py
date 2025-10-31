import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  # 新增：用于绘图

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
# ---------------------- 全局配置与页面设置 ----------------------
st.set_page_config(
    page_title="学生成绩分析与预测系统",
    page_icon="🎠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------------------- 数据加载与预处理 ----------------------
@st.cache_data
def load_data():
    # 替换为你的数据路径
    df = pd.read_csv("student_data_adjusted_rounded.csv")
    # 筛选有效特征（排除学号，避免独热编码爆炸）
    df = df[['性别', '专业', '每周学习时长（小时）', '上课出勤率', '期中考试分数', '作业完成率', '期末考试分数']]
    return df

df = load_data()

# 构建模型训练管道（类别特征独热编码 + 线性回归）
categorical_cols = ['性别', '专业']
numerical_cols = ['每周学习时长（小时）', '上课出勤率', '期中考试分数', '作业完成率']

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(drop='first', sparse_output=False), categorical_cols),
        ('num', 'passthrough', numerical_cols)
    ]
)

model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# 训练模型
X = df.drop('期末考试分数', axis=1)
y = df['期末考试分数']
model.fit(X, y)

# ---------------------- 页面导航与内容 ----------------------
st.sidebar.header("导航菜单")
page = st.sidebar.radio("选择页面", ["项目介绍", "专业数据分析", "成绩预测"])

# ---------- 1. 项目介绍页面 ----------
if page == "项目介绍":
    st.title("🚀 学生成绩分析与预测系统")
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.header("🔥 项目概述")
        st.write("本项目是一个基于Streamlit的学生成绩分析平台，通过数据可视化和机器学习技术，帮助教育工作者和学生深入了解学业表现，并预测期末考试成绩。")
        
        st.header("❄️ 主要特点")
        st.markdown("""
        - 📊 数据可视化：多维度展示学生学业数据
        - 📈 专业分析：按专业分类的详细统计分析
        - 🤖 智能预测：基于机器学习模型的成绩预测
        - 🎯 学习建议：根据预测结果提供个性化反馈
        """)
        
        st.header("🪐 项目目标")
        col3, col4, col5 = st.columns(3)
        with col3:
            st.subheader("🎯 目标一：分析影响因素")
            st.write("识别关键学习指标，探索成绩相关因素，提供数据支持决策。")
        with col4:
            st.subheader("📊 目标二：可视化展示")
            st.write("专业对比分析，性别差异研究，学习模式识别。")
        with col5:
            st.subheader("🔮 目标三：成绩预测")
            st.write("机器学习模型，个性化预测，及时干预预警。")
        
        st.header("🔔️ 技术架构")
        st.markdown("""
        - 前端框架：Streamlit
        - 数据处理：Pandas、Numpy
        - 可视化：Plotly、Matplotlib
        - 机器学习：Scikit-learn
        """)
    
    with col2:
        st.image("tu1.png", caption="学生数据分析示意图",width=500)

# ---------- 2. 专业数据分析页面 ----------
elif page == "专业数据分析":
    st.title("📊 专业数据分析")
    st.markdown("---")
    

    # 1. 各专业男女性别比例
    st.header("1. 各专业男女性别比例")
    # 统计每个专业的男女人数
    gender_major = pd.crosstab(df['专业'], df['性别'])
    # 保持原始专业顺序
    gender_major = gender_major.reindex(df['专业'].unique())
    # 用Streamlit内置柱状图展示
    st.bar_chart(gender_major, use_container_width=True)

    # 2. 各专业学习指标对比
    st.header("2. 各专业学习指标对比")
    col6, col7 = st.columns([2, 1])
    with col6:
    # 按专业分组计算平均值
        metrics_data = df.groupby('专业')[['每周学习时长（小时）', '期中考试分数']].mean()
    # 保持原始专业顺序
        metrics_data = metrics_data.reindex(df['专业'].unique())
    # 用Streamlit内置折线图展示
        st.line_chart(metrics_data, use_container_width=True)
    with col7:
        st.subheader("详细数据")
        metrics_table = df.groupby('专业')[['每周学习时长（小时）', '期中考试分数']].mean().reset_index()
        st.dataframe(metrics_table, use_container_width=True)
    
    # 3. 各专业出勤率分析
    st.header("3. 各专业出勤率分析")
    col8, col9 = st.columns([2, 1])
    with col8:
    # 计算各专业平均出勤率
        attendance_data = df.groupby('专业')['上课出勤率'].mean().reset_index()
        attendance_data = attendance_data.set_index('专业')  # 专业作为索引
    # 用Matplotlib绘制热图
        plt.figure(figsize=(10, 6))
        plt.imshow(attendance_data, cmap='viridis', aspect='auto')  # 热图
        plt.colorbar(label='平均出勤率')  # 颜色条
        plt.xticks(ticks=range(len(attendance_data.index)), 
               labels=attendance_data.index, rotation=45)  # 专业名称
        plt.title('各专业平均出勤率')
        st.pyplot(plt.gcf(), use_container_width=True)  # 显示图表
        plt.close()  # 关闭图表避免重叠
    with col9:
        st.subheader("出勤率排名")
        attendance_rank = df.groupby('专业')['上课出勤率'].mean().sort_values(ascending=False).reset_index()
        attendance_rank.columns = ['专业', '平均出勤率']
        st.dataframe(attendance_rank, use_container_width=True)
    
    # 4. 大数据管理专业专项分析
    st.header("4. 大数据管理专业专项分析")
    df_bigdata = df[df['专业'] == '大数据管理']
    col10, col11, col12, col13 = st.columns(4)
    with col10:
        st.metric("平均出勤率", f"{df_bigdata['上课出勤率'].mean()*100:.1f}%")
    with col11:
        st.metric("平均期中分数", f"{df_bigdata['期中考试分数'].mean():.1f}分")
    with col12:
        st.metric("平均作业完成率", f"{df_bigdata['作业完成率'].mean()*100:.1f}%")
    with col13:
        st.metric("平均学习时长", f"{df_bigdata['每周学习时长（小时）'].mean():.1f}小时")
    
    col14, col15 = st.columns(2)
    with col14:
    # 用Matplotlib绘制直方图
        plt.figure(figsize=(10, 6))
        plt.hist(df_bigdata['期末考试分数'], bins=10, color='#22c55e')  # 直方图
        plt.title('大数据管理专业期末成绩分布')
        plt.xlabel('期末考试分数')
        plt.ylabel('学生数量')
        st.pyplot(plt.gcf(), use_container_width=True)
        plt.close()
    with col15:
    # 用Matplotlib绘制箱线图
        plt.figure(figsize=(10, 6))
        plt.boxplot(df_bigdata['每周学习时长（小时）'], 
                    patch_artist=True, 
                    boxprops=dict(facecolor='#14b8a6'))  # 箱线图
        plt.title('大数据管理专业学习时长分布')
        plt.ylabel('每周学习时长（小时）')
        st.pyplot(plt.gcf(), use_container_width=True)
        plt.close()

# ---------- 3. 成绩预测页面 ----------
else:
    st.title("🎬 期末成绩预测")
    st.markdown("---")
    
    st.info("请输入学生的学习信息，系统将预测其期末成绩并提供学习建议")
    
    # 表单输入
    col16, col17 = st.columns(2)
    with col16:
        student_id = st.text_input("学号", "114514")
        gender = st.selectbox("性别", ["男", "女"])
        major = st.selectbox("专业", df['专业'].unique())
    with col17:
        study_hours = st.slider("每周学习时长(小时)", 0.0, 30.0, 10.0, 0.1)
        attendance = st.slider("上课出勤率", 0.0, 1.0, 0.8, 0.01)
        midterm_score = st.slider("期中考试分数", 0.0, 100.0, 70.0, 0.1)
        homework_rate = st.slider("作业完成率", 0.0, 1.0, 0.7, 0.01)
    
    # 预测按钮
    if st.button("预测期末成绩", type="primary"):
        # 构建输入数据
        input_data = pd.DataFrame({
            '性别': [gender],
            '专业': [major],
            '每周学习时长（小时）': [study_hours],
            '上课出勤率': [attendance],
            '期中考试分数': [midterm_score],
            '作业完成率': [homework_rate]
        })
        
        # 预测成绩
        predicted_score = model.predict(input_data)[0]
        predicted_score = max(0, min(100, predicted_score))  # 限制在0-100之间
        
        # 展示结果
        st.markdown("---")
        st.header("📬 预测结果")
        if predicted_score >= 60:
            st.success(f"预测期末成绩: {predicted_score:.1f}分")
            st.image("999.jpg",width=1000,
                     caption="恭喜你，期末成绩及格啦！肥肥得吃",
                     )
            st.info("学习建议：保持当前学习节奏，向更高的目标出发吧。")
        else:
            st.error(f"预测期末成绩: {predicted_score:.1f}分")
            st.image("888.jpg",width=1000,
                     caption="可惜啊，期末挂科了，再接再厉吧。",
                     )
            st.warning("学习建议：再接再厉，多操作实践和学习吧！。")
