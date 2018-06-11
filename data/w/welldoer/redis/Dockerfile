FROM ubuntu:14.04  
MAINTAINER welldoer  
ENV REFRESHED_AT 2014-12-06  
RUN apt-get -yqq update && apt-get -yqq install redis-server redis-tools  
  
EXPOSE 6379  
ENTRYPOINT ["/usr/bin/redis-server"]  
CMD []  

