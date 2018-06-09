FROM python:2  
MAINTAINER Toni Pohl <info@toni-pohl.de>  
  
RUN mkdir /data-generator  
COPY src/ /data-generator/  
  
WORKDIR /data-generator  
RUN pip install -r requirements.txt  
  
CMD ["python", "main.py"]

