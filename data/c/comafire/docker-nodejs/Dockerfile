FROM node:boron  
MAINTAINER comafire <comafire@gmail.com>  
  
# Bash  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
USER root  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y --no-install-recommends \  
apt-utils \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# Common  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential vim curl wget git cmake bzip2 sudo locales unzip net-tools \  
libffi-dev libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev
llvm \  
libfreetype6-dev libxft-dev  
RUN apt-get update && apt-get install -y --no-install-recommends \  
software-properties-common libjpeg-dev libpng-dev ncurses-dev imagemagick \  
libgraphicsmagick1-dev libzmq-dev gfortran gnuplot gnuplot-x11 libsdl2-dev \  
apt-utils openssh-client htop  
  
# Env  
VOLUME /root/volume  
  
EXPOSE 8080  
WORKDIR /root/volume  
CMD ["./run_nodejs.sh"]  
  

