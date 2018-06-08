FROM python:alpine  
  
RUN adduser -D aws  
  
WORKDIR /home/aws  
  
RUN pip install --upgrade pip  
  
RUN pip install awscli  
  
USER aws  

