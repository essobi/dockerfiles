#  
# Author: Rohith  
# Date: 2015-06-10 12:02:06 +0100 (Wed, 10 Jun 2015)  
#  
# vim:ts=2:sw=2:et  
#  
FROM gliderlabs/alpine:latest  
MAINTAINER Rohith <gambol99@gmail.com>  
  
RUN apk-install bash openssl && \  
mkdir -p /opt/confd/bin /etc/confd/conf.d /etc/confd/templates && \  
wget -q
https://github.com/kelseyhightower/confd/releases/download/v0.9.0/confd-0.9.0-linux-
amd64 -O /opt/confd/bin/confd && \  
ln -s /opt/confd/bin/confd /bin/confd && \  
chmod +x /opt/confd/bin/confd  
  

