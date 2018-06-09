FROM robo2025/python:3.6-alpine  
ENV PYTHONUNBUFFERED 1  
COPY timer/ /project/timer  
  
WORKDIR /project/timer  
  
RUN pip install --upgrade pip  
  
RUN pip install -r requirements.txt -i https://pypi.douban.com/simple  
  
CMD python server.py

