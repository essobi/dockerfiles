#SET THE BASE IMAGE  
FROM alpine  
  
#Dockerfile author / maintainer  
MAINTAINER Keir <keir.asher@gmail.com>  
  
#RUN APPLICATION REPOSITORY LIST AND INSTALL THE SQUID SERVER  
RUN apk add --no-cache squid vim bash  
  
ENV SQUID_CACHE_DIR=/var/cache/squid \  
SQUID_LOG_DIR=/var/log/squid \  
SQUID_USER=squid  
  
  
COPY squid.conf /etc/squid/squid.conf  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
  
#EXPOSE THE DEFAULT PORT  
EXPOSE 3128  
VOLUME ["${SQUID_CACHE_DIR}"]  
  
#SET THE DEFAULT COMMAND  
ENTRYPOINT ["/sbin/entrypoint.sh"]  

