FROM ubuntu:16.04  
MAINTAINER Mike Stead  
  
ENV OCTO_TOOLS_VERSION 4.15.1  
RUN apt-get update && \  
apt-get install -y wget libunwind8 libicu55 libcurl4-openssl-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
cd /opt && \  
wget https://download.octopusdeploy.com/octopus-
tools/$OCTO_TOOLS_VERSION/OctopusTools.$OCTO_TOOLS_VERSION.ubuntu.16.04-x64.tar.gz
&& \  
tar xvf OctopusTools.$OCTO_TOOLS_VERSION.ubuntu.16.04-x64.tar.gz && \  
ln -s /opt/Octo /usr/local/bin/octo && \  
rm OctopusTools.$OCTO_TOOLS_VERSION.ubuntu.16.04-x64.tar.gz  
  
WORKDIR /home  

