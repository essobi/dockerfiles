FROM lysender/php  
MAINTAINER Leonel Baer <leonel@lysender.com>  
  
# Install Apache and misc tools  
RUN yum -y update && \  
yum -y install supervisor \  
httpd \  
make \  
openssl \  
mod_ssl \  
nodejs \  
npm \  
libevent \  
gearmand \  
libgearman \  
libgearman-devel \  
php-pecl-gearman \  
libmemcached \  
php-pecl-memcached && yum clean all  
  
# Add node packages for minifiers  
RUN npm install -g uglify-js && \  
npm install -g uglifycss  
  
# Add config files and scripts  
ADD ./vhost.conf /etc/httpd/conf.d/default-vhost.conf  
ADD ./index.php /var/www/html/index.php  
  
# Configure services  
ADD ./start.sh /start.sh  
RUN chmod 0777 /start.sh  
ADD ./supervisor-httpd.ini /etc/supervisord.d/httpd.ini  
  
RUN chmod 755 /start.sh  
  
VOLUME ["/var/www/html", "/var/log/httpd"]  
  
EXPOSE 80  
CMD ["/bin/bash", "/start.sh"]  
  

