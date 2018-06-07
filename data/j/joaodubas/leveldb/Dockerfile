# leveldb  
#  
# VERSION: see `TAG`  
FROM debian:jessie  
MAINTAINER Joao Paulo Dubas "joao.dubas@gmail.com"  
# install system deps  
RUN apt-get -y -qq --force-yes update \  
&& apt-get -y -qq --force-yes install libleveldb-dev libleveldb1  
  
# cleanup  
RUN apt-get -y -qq --force-yes clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

