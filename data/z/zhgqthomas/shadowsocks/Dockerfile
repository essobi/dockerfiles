# shadowsocks  
#  
# VERSION 1.0.4  
FROM debian:jessie  
MAINTAINER Thomas <zhgqthomas@gmail.com>  
  
# add Debian jessie backports  
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" \  
| tee /etc/apt/sources.list.d/backports.list \  
# update repository & upgrade dependencies & install shadowsocks-libev  
&& apt-get update \  
&& apt-get -t jessie-backports install -y shadowsocks-libev  
  
# Configure container to run as an executable  
ENTRYPOINT ["/usr/bin/ss-server"]  

