FROM python:3.6.1  
MAINTAINER zheng zxyful@gmail.com  
  
ENV ENV PROD  
  
WORKDIR /code  
  
COPY requirements/*.txt ./  
  
RUN pip install --no-cache-dir -r common.txt  
  
VOLUME ["/program", "/code"]

