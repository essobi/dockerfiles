FROM ubuntu:16.04  
MAINTAINER Olof Nilsson <olof@drp.nu>  
  
# Workaround to get rid of ugly red text when building from Dockerfile  
ENV DEBIAN_FRONTEND "noninteractive"  
# Install usual dependencies and "nice to have", followed by cleanup  
RUN apt-get update -q && \  
apt-get upgrade -qy && \  
apt-get install -qy \  
build-essential \  
software-properties-common \  
curl \  
git \  
htop \  
vim \  
wget && \  
apt-get clean  
  
# Defaults  
ENV HOME /root  
WORKDIR /root  
  
# Default Command  
CMD ["bash"]  

