FROM phusion/baseimage:0.9.15  
MAINTAINER Juan B. Rodriguez <jbrodriguez@apertoire.net>  
  
# Set correct environment variables  
ENV DEBIAN_FRONTEND=noninteractive LC_ALL=C.UTF-8 LANG=en_US.UTF-8
LANGUAGE=en_US.UTF-8 HOME=/root  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
ADD install.sh /tmp/install.sh  
RUN chmod +x /tmp/install.sh && /tmp/install.sh  
  
VOLUME /config /mnt /root  
EXPOSE 6237  
  

