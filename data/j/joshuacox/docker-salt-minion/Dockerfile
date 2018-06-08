FROM debian:wheezy  
MAINTAINER Josh Cox <josh 'at' webhosting coop>  
  
ENV DOCKER_SALT_MINION 20150513  
# If you set a SALT_MASTER it will use that automatically  
# ENV SALT_MASTER 127.0.0.1  
ADD ./scripts /scripts  
RUN chmod 755 /scripts/*.sh  
RUN cd /;/bin/sh -c /scripts/install.sh  
# Define default command.  
CMD ["/scripts/start.sh"]  

