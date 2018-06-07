FROM python:2.7-alpine  
  
MAINTAINER xausky xausky@gmail.com  
  
RUN pip install docker-py  
  
ADD app /app  
  
WORKDIR /app  
  
CMD ["python","main.py"]  

