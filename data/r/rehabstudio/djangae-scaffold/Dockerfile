FROM rehabstudio/gcloud  
MAINTAINER Noel Wilson <noel.wilson@rehabstudio.com>  
  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y libfontconfig && \  
apt-get install -y software-properties-common && \  
apt-get install -y libssl-dev && \  
apt-get install -y libffi-dev && \  
apt-get install -y libxml2-dev && \  
apt-get install -y libjpeg62-turbo-dev && \  
apt-get install -y python-setuptools && \  
apt-get install -y python-virtualenv && \  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 8081 8000 8080 35607  

