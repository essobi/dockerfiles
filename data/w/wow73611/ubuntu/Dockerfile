FROM ubuntu:14.04  
MAINTAINER wow73611 <wow73611@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN \  
apt-get update -y && \  
apt-get upgrade -y && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y python-software-properties && \  
apt-get install -y vim wget curl && \  
rm -rf /var/lib/apt/lists/*  
  
CMD ["bash"]  

