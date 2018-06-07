FROM debian:stretch  
MAINTAINER Paul Woelfel <github@frig.at>  
  
RUN apt-get update && apt-get -y upgrade && \  
apt-get -y install \  
apt-transport-https \  
ca-certificates \  
curl \  
gettext \  
gnupg2 \  
software-properties-common \  
curl \  
wget \  
&& \  
(curl -sL https://deb.nodesource.com/setup_7.x | bash -) && \  
apt-get -y install \  
nodejs \  
&& \  
npm install -g bower && \  
(echo "deb https://packages.cloud.google.com/apt cloud-sdk-$(lsb_release -c
-s) main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list) && \  
(curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -)
&& \  
apt-get update && \  
apt-get -y install \  
google-cloud-sdk \  
google-cloud-sdk-app-engine-python \  
git \  
python \  
python-crypto \  
python-pip \  
&& \  
pip install pycrypto && \  
(curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -) && \  
(add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/debian \  
$(lsb_release -cs) \  
stable") && \  
apt-get update && \  
apt-get -y install \  
docker-ce && \  
rm -rf /var/lib/apt/lists/*  
  
ENV ENDPOINTS_GAE_SDK /usr/lib/google-cloud-sdk  

