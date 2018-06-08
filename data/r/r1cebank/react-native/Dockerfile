############################################################  
# Dockerfile to run build React Native Packager image  
# Based on node  
############################################################  
  
FROM node:argon  
  
# File Author / Maintainer  
MAINTAINER Siyuan Gao <siyuangao@gmail.com>  
  
RUN apt-get update && \  
apt-get -y install software-properties-common git-core build-essential
automake unzip python-dev python-setuptools && \  
rm -rf /var/lib/apt/lists/*  
  
RUN git clone -b v3.8.0 https://github.com/facebook/watchman.git /tmp/watchman  
WORKDIR /tmp/watchman  
RUN ./autogen.sh  
RUN ./configure  
RUN make  
RUN make install  
  
EXPOSE 8081  
  
  
CMD ["npm", "start"]  

