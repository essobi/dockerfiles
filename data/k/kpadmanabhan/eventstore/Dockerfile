# Based on documentation from geteventstore.com  
#Reference: http://docs.geteventstore.com/server/3.2.0/installing-from-debian-
repositories/  
FROM ubuntu:14.04  
MAINTAINER P Karthikeyan <@humblelistener>  
  
ENV ES_VERSION v3.2.0  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -qq update \  
&& apt-get install -qq curl apt-transport-https  
  
RUN curl -sS https://apt-oss.geteventstore.com/eventstore.key | apt-key add -  
  
RUN echo "deb [arch=amd64] https://apt-oss.geteventstore.com/ubuntu/ trusty
$ES_VERSION" > /etc/apt/sources.list.d/eventstore.list \  
&& apt-get -qq update \  
&& apt-get -qq install eventstore-oss  
  
VOLUME /data/db /data/logs  
  
COPY eventstore.conf /etc/eventstore/  
  
# downstream builds can use their own evenstore.conf  
ONBUILD COPY eventstore.conf /etc/eventstore/  
  
EXPOSE 2113  
EXPOSE 1113  
ENTRYPOINT exec /usr/bin/eventstored  

