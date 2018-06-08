FROM ubuntu:16.04  
MAINTAINER "Piero Giusti <pierophp@gmail.com>"  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
  
# Upgrade  
RUN apt update && \  
apt upgrade -y && \  
apt clean && rm -rf /var/lib/apt/lists/*  
# Tools  
RUN apt update && \  
apt install -y wget curl vim nano less unzip git mlocate lsof && \  
apt clean && rm -rf /var/lib/apt/lists/*  
#Add user  
RUN useradd -ms /bin/bash dev -G sudo,ssh && echo 'dev:123' | chpasswd

