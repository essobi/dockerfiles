# Shadowsocks libev with Debian  
FROM debian:wheezy  
MAINTAINER iceihehe "iceihehe@gmail.com"  
# add GPG public key  
RUN apt-get update && apt-get install -y wget  
RUN wget -O- http://shadowsocks.org/debian/1D27208A.gpg | apt-key add -  
RUN apt-get --purge autoremove -y wget  
  
# enable backports  
RUN echo "deb http://ftp.debian.org/debian wheezy-backports main" >>
/etc/apt/sources.list  
# add shadowsocks repository  
RUN echo "deb http://shadowsocks.org/debian wheezy main" >>
/etc/apt/sources.list  
  
# install shadowsocks-libev  
RUN apt-get update && apt-get install -y init-system-helpers shadowsocks-libev  
  
EXPOSE 1080 8388  

