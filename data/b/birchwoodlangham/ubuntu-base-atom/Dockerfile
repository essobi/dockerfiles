FROM birchwoodlangham/ubuntu-base-ui:latest  
  
MAINTAINER Tan Quach <tan.quach@birchwoodlangham.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y -qq python-dev && \  
apt-get clean && rm -rf /var/lib/apt/lists/* && \  
wget https://github.com/atom/atom/releases/download/v1.26.1/atom-amd64.deb &&
\  
dpkg -i atom-amd64.deb && \  
rm atom-amd64.deb  

