FROM python:3.9-slim
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt -i https://mirrors.bfsu.edu.cn/pypi/web/simple
CMD ["python", "bot.py"]