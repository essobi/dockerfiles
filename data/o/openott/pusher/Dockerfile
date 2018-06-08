FROM python:2-slim  
MAINTAINER Viknet <viknet@icloud.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -q && \  
apt-get install -qqy librados2  
  
WORKDIR /app  
  
COPY . /app  
  
ENTRYPOINT ["./pusher.py"]  

