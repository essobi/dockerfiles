#  
# Ubuntu Dockerfile  
# version 1.1  
#  
FROM ubuntu:16.04  
MAINTAINER Leo <jiangwenhua@yoyohr.com>  
  
#Update sources.list  
COPY sources.list /etc/apt/sources.list  
  
# Install packages  
RUN apt-get update \  
&& DEBIAN_FRONTEND="noninteractive" \  
apt-get dist-upgrade -y \  
&& DEBIAN_FRONTEND="noninteractive" \  
apt-get install -y \  
ca-certificates \  
curl \  
libpcre3 \  
librecode0 \  
libsqlite3-0 \  
libxml2 \  
\--no-install-recommends \  
&& DEBIAN_FRONTEND="noninteractive" \  
apt-get autoremove -y \  
&& DEBIAN_FRONTEND="noninteractive" \  
apt-get autoclean -y \  
&& rm -rf /var/lib/apt/lists/*  
  

