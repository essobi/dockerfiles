FROM ubuntu:14.04  
MAINTAINER wenzizone <wenzizone@126.com>  
  
#ADD sources.list /etc/apt/sources.list  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y ca-certificates inotify-tools supervisor unzip wget curl &&
\  
apt-get clean

