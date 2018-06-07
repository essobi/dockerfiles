FROM ubuntu:14.04  
# Install packages  
ADD create_memcached_admin_user.sh /create_memcached_admin_user.sh  
ADD provision.sh /provision.sh  
ADD run.sh /run.sh  
  
RUN chmod +x /*.sh  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN ./provision.sh  
  
EXPOSE 80  
CMD ["/run.sh"]  

