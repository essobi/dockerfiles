FROM ubuntu:latest  
  
MAINTAINER Petr Moravek  
  
# Set correct environment variables.  
# COLUMNS=80 \  
# LINES=24 \  
# container=docker \  
ENV HOME=/root \  
TERM=xterm-256color \  
PXL_VER=vmware-tools-1.0 \  
DEBIAN_FRONTEND=noninteractive  
  
ADD include/ /root/  
  
RUN sh -C /root/01-base.sh 1>&2  
RUN sh -C /root/02-addUser.sh 1>&2  
RUN sh -C /root/03-addDebs.sh 1>&2  
RUN sh -C /root/04-addCpanMods.sh 1>&2  
  
ADD include/loopForEver /usr/local/bin/  
  
ENV HOME /host  
WORKDIR /host  
USER user  

