FROM ubuntu:latest  
  
# ---  
# ---  
# ---  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y \  
curl \  
git \  
build-essential \  
pkg-config \  
python python-dev \  
libkrb5-dev \  
libcairo2-dev \  
libjpeg-dev \  
libgif-dev && \  
apt-get clean  
  
# ---  
# ---  
# ---  
RUN curl --location https://bootstrap.pypa.io/get-pip.py | python  
  
RUN pip install awscli awsebcli  
  
# ---  
# ---  
# ---  
RUN curl --location https://deb.nodesource.com/setup_9.x | bash -  
  
RUN apt-get install -y nodejs  
  
RUN npm install -g grunt-cli@0.1.13 \  
s3-upload@0.0.3 \  
cloudflare-cli@1.4.0 \  
wintersmith@2.2.1 wintersmith-less@0.2.3 wintersmith-browserify@0.9.0  
  
# ---  
# ---  
# ---  
WORKDIR /root/  
  
# ---  

