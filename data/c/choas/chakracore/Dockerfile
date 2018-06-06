#  
# ChakraCore Dockerfile  
# https://github.com/choas/chakracore-docker  
#  
# base image  
# based on release notes https://github.com/nodejs/node-
chakracore/releases/tag/node-chakracore-xplat-7.0.0-pre8  
FROM ubuntu:16.04  
# Install.  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y wget libunwind8 libicu55 && \  
wget https://github.com/nodejs/node-chakracore/releases/download/node-
chakracore-xplat-7.0.0-pre8/node-chakracore_7.0.0-pre8-Ubuntu16.04_amd64.deb
&& \  
dpkg -i node-chakracore_7.0.0-pre8-Ubuntu16.04_amd64.deb && \  
rm node-chakracore_7.0.0-pre8-Ubuntu16.04_amd64.deb && \  
rm -rf /var/lib/apt/lists/* && \  
node -v  

