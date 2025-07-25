# 使用官方 Python 基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 安装依赖前先复制 requirements.txt
COPY requirements.txt .

# 安装依赖（用国内源加速可以选用清华源）
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

# 再复制项目所有文件
COPY . .

# 暴露 FastAPI 默认端口
EXPOSE 8000

# 启动命令（请确保 weaver_api.py 存在且 app 对象定义了）
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]

# docker build -t weaver-api .
# docker run -d -p 8000:8000 --name weaver_api weaver-api
