# Data only container for mariadb.  
#  
# See: http://www.tech-d.net/2013/12/16/persistent-volumes-with-docker-
container-as-volume-pattern/  
# for more information.  
  
FROM busybox  
MAINTAINER Laurens Duijvesteijn <l.duijvesteijn@gmail.com>  
  
# Create /var/lib/mysql directory  
RUN mkdir -p /var/lib/mysql  
# Create /var/lib/mysql volume  
VOLUME /var/lib/mysql  

