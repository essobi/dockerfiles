FROM ubuntu:14.04  
MAINTAINER Kai Hofstetter <kai.hofstetter@gmx.de>  
  
RUN apt-get update && \  
apt-get install -y curl libneon27-gnutls libapr1 libaprutil1 libserf-1-1  
  
RUN curl -L
"http://launchpadlibrarian.net/161750374/subversion_1.7.14-1ubuntu2_amd64.deb"
> subversion_1.7.14.deb  
RUN curl -L
"http://launchpadlibrarian.net/161750375/libsvn1_1.7.14-1ubuntu2_amd64.deb" >
libsvn_1.7.14.deb  
  
RUN dpkg -i libsvn_1.7.14.deb  
RUN dpkg -i subversion_1.7.14.deb  
  
RUN echo "store-plaintext-passwords = no" >> /etc/subversion/servers  

