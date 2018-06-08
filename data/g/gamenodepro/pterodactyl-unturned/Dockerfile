FROM debian:latest  
  
MAINTAINER Isaac A, <isaac@isaacs.site>  
  
RUN dpkg --add-architecture i386 && \  
apt update && \  
apt upgrade -y && \  
apt install -y unzip libreadline5 libncursesw5 lib32ncursesw5 lib32stdc++6 &&
\  
useradd -d /home/container -m container  
  
USER container  
ENV  USER container  
ENV HOME /home/container  
  
WORKDIR /home/container  

