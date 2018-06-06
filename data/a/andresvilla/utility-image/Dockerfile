FROM ubuntu:16.04  
MAINTAINER Andres Villa <andresfvilla88@gmail.com>  
  
#Install dependencies  
#This is used to generate load on the clients  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y \  
ansible \  
curl \  
default-jre \  
default-jdk \  
dnsutils \  
iperf \  
iputils-ping \  
kmod \  
mtr \  
netcat \  
nodejs \  
npm \  
python \  
vim \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
#Install Node 9.x  
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash -  
RUN apt-get update \  
&&apt-get install --no-install-recommends -y \  
nodejs \  
&& rm -rf /var/lib/apt/lists/*  
#requires unsafe due to npm having permission problems from "unnamed" user  
RUN npm install -g grpcc --unsafe  
  
# #Install cuda  
# COPY cuda-repo-ubuntu1604_9.0.176-1_amd64.deb /opt/cuda-repo-
ubuntu1604_9.0.176-1_amd64.deb  
# RUN dpkg -i /opt/cuda-repo-ubuntu1604_9.0.176-1_amd64.deb \  
# && apt-get update \  
# && apt-get install -y --allow-unauthenticated \  
# cuda-toolkit-8-0 \  
# && rm -rf /var/lib/apt/lists/*  
  
CMD ["tail", "-F", "-n0", "/etc/hosts"]  

