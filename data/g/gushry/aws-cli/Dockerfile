FROM python:3.5.0-slim  
MAINTAINER gushry  
  
RUN apt-get update && apt-get install -y curl \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "/tmp/get-pip.py" \  
&& python /tmp/get-pip.py \  
&& rm -rf /tmp/get-pip.py \  
&& pip install awscli  
  
ENV LANG ja_JP.UTF-8  
  
RUN env  

