FROM node:6  
RUN \  
apt-get update \  
&& apt-get install -y --no-install-recommends \  
ssh \  
wget \  
git \  
vim \  
wget \  
zlib1g-dev \  
jq \  
build-essential \  
iptables \  
libapparmor1 \  
libltdl7 \  
libmcrypt-dev \  
libxml2-dev \  
zip \  
unzip \  
python \  
python-dev \  
python-pip \  
python-yaml \  
redis-server \  
&& apt-get clean  
  
RUN python -v  
RUN pip -v  
  
RUN pip install awscli --upgrade  
  
RUN npm install -g yarn --update && yarn global add lambda-local babel-preset-
env node-lambda --latest  
  
RUN wget
https://github.com/andreyk0/kms-s3/releases/download/v0.5/kms-s3-Linux-x86_64  
RUN chmod +x kms-s3-Linux-x86_64  
RUN mv kms-s3-Linux-x86_64 /usr/bin/kms-s3  
RUN kms-s3 -h  
  

