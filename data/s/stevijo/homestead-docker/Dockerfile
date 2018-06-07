FROM guilhem/vagrant-ubuntu:14.04  
# Install packages  
ADD create_memcached_admin_user.sh /create_memcached_admin_user.sh  
ADD provision.sh /provision.sh  
ADD run.sh /run.sh  
  
RUN chmod +x /*.sh  
  
RUN ./provision.sh  
  
EXPOSE 80 22 5432 35729 27017  
CMD ["/run.sh"]  

