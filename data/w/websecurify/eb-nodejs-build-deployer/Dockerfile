FROM ubuntu:15.04  
# ---  
# ---  
# ---  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y \  
curl \  
git \  
build-essential \  
python python-dev \  
libkrb5-dev && \  
apt-get clean  
  
# ---  
# ---  
# ---  
RUN curl --location https://bootstrap.pypa.io/get-pip.py | python  
  
RUN pip install awscli awsebcli  
  
# ---  
# ---  
# ---  
RUN curl --location https://deb.nodesource.com/setup_0.12 | bash -  
  
RUN apt-get install -y nodejs  
  
RUN npm install -g grunt-cli  
  
# ---  
# ---  
# ---  
WORKDIR /root/  
  
# ---  

