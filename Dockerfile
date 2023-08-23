# 使用基础镜像
FROM python:3.8

# 设置工作目录
WORKDIR /app

# 复制应用程序代码到容器
COPY . /app

# 安装应用程序依赖
RUN pip install -r requirements.txt

# 声明应用程序运行命令
CMD ["python", "test_runner.py"]
