import streamlit as st
import pandas as pd
import os


# 从指定路径读取Excel文件
file_path = r"D:\BIT课题研究\微型光谱成像仪\【数据】导电聚合物数据\方案设计\原材料数据库\EC合成化学品数据20230619.xlsx"
df = pd.read_excel(file_path)
# 获取文件名
file_name = os.path.basename(file_path)
# 获取Excel文件的所有sheet名称
sheet_names = pd.ExcelFile(file_path).sheet_names

# Streamlit应用
# 设置页面宽度
st.set_page_config(layout="wide")
# 使用文件名作为标题
st.title(file_name)

# 依次读取并显示每个sheet的数据
for sheet_name in sheet_names:
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    st.subheader(sheet_name)
    # 使用st.dataframe显示表格
    st.dataframe(df)

# 可以根据需要添加其他交互元素或可视化组件
