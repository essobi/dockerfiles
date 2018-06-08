############################################################  
# Dockerfile to build Python WSGI Application Containers  
############################################################  
  
FROM travix/base-debian:latest  
  
MAINTAINER Travix  
RUN apt-get update && apt-get install -y \  
build-essential \  
curl \  
git \  
python3-dev \  
python3-pip \  
vim \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN git clone https://github.com/Travix-International/flamock.git  
  
WORKDIR /flamock  
RUN pip3 install -r requirements.txt  
  
# Expose ports  
EXPOSE 1080 8801 8802 8805  
  
# Setup for pipeline  
CMD /bin/bash ./startup.sh;

