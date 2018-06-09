FROM python:2.7  
MAINTAINER Markus Mayer <widemeadows@gmail.com>  
  
RUN mkdir /app  
WORKDIR /app  
  
COPY requirements.txt /app  
COPY wakamon.py /app  
  
RUN pip install -r requirements.txt  
  
CMD python wakamon.py

