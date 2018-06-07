FROM python:3.4-alpine  
  
RUN apk add -U \  
gcc \  
linux-headers \  
musl-dev \  
&& \  
pip install uwsgi && \  
apk del \  
gcc \  
linux-headers \  
musl-dev  

