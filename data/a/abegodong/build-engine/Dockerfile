FROM ubuntu:16.04  
MAINTAINER Abraham Godong <abrahamg@strategies360.com>  
  
RUN apt update && apt -y upgrade && \  
apt -y install \  
apt-transport-https \  
ca-certificates \  
curl \  
wget \  
gnupg2 \  
libpng-dev \  
&& \  
(curl -sL https://deb.nodesource.com/setup_7.x | bash -) && \  
apt -y install nodejs && \  
npm install -g bower gulp && \  
(echo "deb https://packages.cloud.google.com/apt cloud-sdk-$(lsb_release -c
-s) main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list) && \  
(curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -)
&& \  
apt update && \  
apt -y install \  
google-cloud-sdk \  
google-cloud-sdk-app-engine-python \  
git \  
python \  
python-crypto \  
python-pip \  
&& \  
pip install pycrypto && \  
rm -rf /var/lib/apt/lists/*  
  
ENV ENDPOINTS_GAE_SDK /usr/lib/google-cloud-sdk

