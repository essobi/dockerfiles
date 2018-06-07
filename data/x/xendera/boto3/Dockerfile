FROM python:3.6-alpine  
LABEL maintainer="Xendera Team <hello@xendera.com>"  
  
WORKDIR /usr/src/app  
  
ONBUILD RUN pip install boto3  
ONBUILD COPY requirements.txt /usr/src/app/  
ONBUILD RUN pip install --no-cache-dir -r requirements.txt  

