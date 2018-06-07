FROM debian:testing  
  
MAINTAINER Stefan Bühler <stbuehler@lighttpd.net>  
  
# don't install recommended dependencies  
COPY apt.conf.no-recommends /etc/apt/apt.conf.d/no-recommends  
  
# build essentials  
RUN apt-get update \  
&& DEBCONF_FRONTEND='noninteractive' apt-get install -y build-essential  

