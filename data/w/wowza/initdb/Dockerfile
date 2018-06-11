# basic usage  
# docker run --link db wowza/initdb bash -c "`cat initdb.sh`"  
  
FROM wowza/debian:jessie  
MAINTAINER Tom Davidson <tom.davidson@wowza.com>  
  
RUN apt-get update && apt-get -y install \  
mariadb-client \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

