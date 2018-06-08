FROM ubuntu:latest  
  
MAINTAINER Curt H., <curt@curtcreation.net>  
  
RUN apt update && \  
apt upgrade -y && \  
apt install -y lib32gcc1 unzip curl libreadline5 libncursesw5 lib32ncursesw5
lib32stdc++6 wget libstdc++6 software-properties-common && \  
add-apt-repository "ppa:ubuntu-toolchain-r/test" -y && \  
apt-get update && \  
apt-get install -y gcc-6 g++-6 && \  
useradd -d /home/container -m container  
  
USER container  
ENV  USER container  
ENV HOME /home/container  
WORKDIR /home/container  
COPY ./entrypoint.sh /entrypoint.sh  
CMD ["/bin/bash", "/entrypoint.sh"]  

