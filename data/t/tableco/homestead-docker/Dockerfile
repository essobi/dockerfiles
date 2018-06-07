FROM ubuntu:14.04  
MAINTAINER info@table.co  
  
# Install packages  
ADD provision.sh /provision.sh  
ADD serve.sh /serve.sh  
ADD run.sh /run.sh  
  
RUN chmod +x /*.sh  
  
RUN ./provision.sh  
  
EXPOSE 80  
CMD ["/run.sh"]  
#ENTRYPOINT /usr/sbin/php-fpm --nodaemonize  

