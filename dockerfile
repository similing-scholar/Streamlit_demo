# 从python3.6镜像基础上创建
FROM python:3.6
# Streamlit 应用默认的端口
EXPOSE 8501
# 设置容器内的工作目录
WORKDIR /Streamlit_demo
# 将主机上的requirements.txt文件复制到容器内,安装依赖。
COPY requirements.txt ./requirements.txt
# 设置镜像源，提高pip install 速度
RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/ \
        && pip install -r requirements.txt
# 将当前目录中的所有文件复制到容器的当前工作目录
COPY . .
# 指定了容器启动后要运行的默认命令
CMD streamlit run test0.py

