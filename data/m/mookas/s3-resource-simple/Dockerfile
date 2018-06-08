FROM python:3.5-alpine  
  
RUN apk add --update jq bash && \  
pip install --upgrade pip && \  
pip install --upgrade awscli  
  
ADD assets/ /opt/resource/  

