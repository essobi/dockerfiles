FROM ubuntu:xenial  
MAINTAINER Leonel Baer <leonel@lysender.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update && \  
apt-get -y install curl && \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get -y update && \  
apt-get -y install nodejs && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
CMD ["node"]  
  

