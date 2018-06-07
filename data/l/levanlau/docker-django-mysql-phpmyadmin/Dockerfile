FROM python:3.5  
MAINTAINER LauLe "vanlau.le@gmail.com"  
ENV PYTHONUNBUFFERED 1  
RUN mkdir /public_html  
WORKDIR /public_html  
ADD requirements.txt /public_html/  
RUN pip install -r requirements.txt  
ADD . /public_html/  

