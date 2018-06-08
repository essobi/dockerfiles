FROM lysender/php  
MAINTAINER Leonel Baer <leonel@lysender.com>  
  
RUN yum -y install supervisor \  
libevent \  
libgearman \  
libgearman-devel \  
php-pecl-gearman \  
libmemcached \  
php-pecl-memcached \  
java-1.8.0-openjdk \  
mysql-connector-java \  
liquibase && yum clean all  
  
# Configure blank services and let the mounted files do the work  
ADD ./start.sh /start.sh  
RUN chmod 755 /start.sh  
  
VOLUME ["/data", "/var/log/supervisor"]  
CMD ["/bin/bash", "/start.sh"]  
  

