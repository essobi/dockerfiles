FROM ubuntu:trusty  
MAINTAINER Ian Lintner <ian.lintner@workiva.com>  
  
#install memcached  
RUN apt-get update && \  
apt-get install -y libevent-dev && \  
apt-get install -y memcached && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
#ADD create_memcached_admin_user.sh /create_memcached_admin_user.sh  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
  
USER memcache  
EXPOSE 11211  
CMD ["/run.sh"]  

