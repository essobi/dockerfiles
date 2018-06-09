FROM rancher/vm-ubuntu:14.04  
RUN apt-get update && \  
apt-get install -y git && \  
git clone https://github.com/apache/incubator-openwhisk.git openwhisk  
  
COPY docker.sh openwhisk/tools/ubuntu-setup/docker.sh  
  
RUN cd openwhisk/tools/ubuntu-setup && ./all.sh  
  

