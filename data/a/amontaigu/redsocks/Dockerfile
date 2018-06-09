#
=================================================================================  
#  
# Docker redsocks image.  
#  
# @see https://github.com/hiroakis/docker-sensu-server  
# @see https://sensuapp.org/docs/latest/install-sensu  
#
=================================================================================  
# Base image  
FROM debian:jessie  
  
# Maintainer  
MAINTAINER Alban Montaigu <https://github.com/AlbanMontaigu/docker-redsocks>  
  
# Configuration  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install packages  
RUN apt-get update && apt-get install -y redsocks iptables  
  
# Copy configuration files...  
COPY redsocks/redsocks.tmpl /etc/redsocks.tmpl  
COPY redsocks/whitelist.txt /etc/redsocks-whitelist.txt  
COPY redsocks/redsocks.sh /usr/local/bin/redsocks.sh  
COPY redsocks/redsocks-fw.sh /usr/local/bin/redsocks-fw.sh  
  
# To prevent chmod issue  
RUN chmod +x /usr/local/bin/*  
  
# Main command  
ENTRYPOINT ["/usr/local/bin/redsocks.sh"]  

