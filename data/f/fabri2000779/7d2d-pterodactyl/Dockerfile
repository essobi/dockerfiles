FROM ubuntu:latest  
  
MAINTAINER Fabri2000779 ., <fabri2014@hotmail.com>  
  
RUN dpkg --add-architecture i386 && \  
apt update && \  
apt upgrade -y && \  
apt-get install -y libc6-i386 lib32gcc1 lib32stdc++6 -y unzip curl && \  
useradd -d /home/container -m container  
  
USER container  
ENV  USER container  
ENV HOME /home/container  
  
WORKDIR /home/container  
  
COPY ./entrypoint.sh /entrypoint.sh  
  
CMD ["/bin/bash", "/entrypoint.sh"]  

