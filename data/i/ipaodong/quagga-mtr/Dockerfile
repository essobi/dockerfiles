# This dockerfile uses the ubuntu image  
# VERSION 1 - EDITION 1  
# Author: ipaodong  
# Base image to use, this must be set as the first line  
FROM ubuntu:14.04  
# Maintainer: docker_user <docker_user at email.com> (@docker_user)  
MAINTAINER ipaodong ipaodong@gmail.com  
  
# Commands to update the image  
ENV LD_LIBRARY_PATH /usr/local/lib  
  
COPY sources.list /etc/apt/sources.list  
RUN apt-get update && apt-get install -y gcc make autoconf automake libtool
intltool gawk texinfo libreadline-dev  
  
COPY quagga-mtr /root/quagga-mtr  
WORKDIR /root/quagga-mtr  
RUN ./bootstrap.sh  
RUN ./configure --enable-vtysh --enable-user=root --enable-group=root  
RUN make -j4 && make install  
RUN cd /usr/local/etc && rename 's/\\.sample//g' *  
  
# Commands when creating a new container  
CMD /bin/bash  

