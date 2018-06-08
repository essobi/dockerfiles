FROM python:3  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN set -eux &&\  
apt-get update &&\  
apt-get upgrade -y &&\  
apt-get install -yq \  
zip &&\  
rm -rf /var/lib/apt-lists/*  

