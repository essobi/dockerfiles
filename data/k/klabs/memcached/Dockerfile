FROM debian:jessie  
MAINTAINER Kaliop  
LABEL memcached.version=1.4  
  
ARG DOCKER_TIMEZONE=Europe/Paris  
  
# Configure timezone  
#
-----------------------------------------------------------------------------  
RUN echo $DOCKER_TIMEZONE > /etc/timezone; dpkg-reconfigure -f noninteractive
tzdata  
  
ENV MEMCACHED_USER=nobody  
  
# Base packages  
#
-----------------------------------------------------------------------------  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
memcached  
  
RUN rm /etc/memcached.conf  
COPY memcached.conf /etc/memcached.conf  
  
RUN chmod 644 /etc/memcached.conf  
  
COPY bootstrap.sh /root/bootstrap.sh  
RUN chmod 755 /root/bootstrap.sh  
  
#
-----------------------------------------------------------------------------  
# Clear archives in apt cache folder  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
EXPOSE 11211/tcp 11211/udp  
  
CMD ["/root/bootstrap.sh"]  

