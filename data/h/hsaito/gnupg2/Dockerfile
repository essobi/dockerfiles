FROM ubuntu:latest  
MAINTAINER Hideki Saito <hideki@hidekisaito.com>  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get -y install git curl pkg-config build-essential libncurses5-dev
bzip2 zlib1g-dev libzip-dev libbz2-dev libldap2-dev libgnutls-dev  
COPY * /root/gnupg-buildkit/  
COPY files /root/gnupg-buildkit/files  
RUN mkdir /root/gnupg-buildkit/.gnupg  
RUN cd /root/gnupg-buildkit && ./updatesig.sh  
RUN cd /root/gnupg-buildkit && ./get.sh  
RUN cd /root/gnupg-buildkit && ./build_nox.sh  
RUN ldconfig  

