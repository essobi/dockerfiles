FROM ubuntu:latest  
LABEL maintainer="Denis Ivanov"  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get -y update && \  
apt-get -y install \  
gcc \  
python3-dev \  
python3-pip && \  
pip3 install gunicorn  
  
# Cleaning  
RUN apt-get -y autoremove && \  
apt-get -y clean  
  
WORKDIR /srv/  
  
ENTRYPOINT [ "gunicorn" ]  

