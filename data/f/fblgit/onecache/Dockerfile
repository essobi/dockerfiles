FROM ubuntu:14.04  
MAINTAINER FBLGIT@GitHub  
ENV DEBIAN_FRONTEND=noninteractive  
RUN apt-get update && apt-get install -qy libjemalloc-dev libevent-dev
autoconf make g++ gcc redis-tools binutils && apt-get clean -qy  
COPY onecache /usr/bin/onecache  
COPY start_docker.sh /start_docker.sh  
COPY onecache.xml /etc/onecache.xml  
CMD ["/start_docker.sh"]  

