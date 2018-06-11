################################################################################  
#  
# Ubunt 16.04  
#  
################################################################################  
  
FROM ubuntu:16.04  
MAINTAINER yingzhuo <yingzhor@gmail.com>  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
##  
# 基本工具  
##  
RUN \  
apt-get update && \  
apt-get install -y curl wget zip unzip tree python-software-properties
software-properties-common && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
##  
# dockerize  
# 参考: https://github.com/jwilder/dockerize  
##  
ENV DOCKERIZE_VERSION v0.2.0  
RUN \  
wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz && \  
tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
CMD ["bash"]  

