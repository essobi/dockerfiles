FROM lysender/php  
MAINTAINER Leonel Baer <leonel@lysender.com>  
  
# Install Apache and misc tools  
RUN yum -y install supervisor \  
httpd \  
make \  
openssl \  
mod_ssl && yum clean all  
  
# Add config files and scripts  
ADD ./vhost.conf /etc/httpd/conf.d/default-vhost.conf  
ADD ./index.php /var/www/html/index.php  
  
# Configure servicies  
ADD ./start.sh /start.sh  
ADD ./supervisor-httpd.ini /etc/supervisord.d/httpd.ini  
  
RUN chmod 755 /start.sh  
  
VOLUME ["/var/www/html", "/var/log/httpd"]  
  
EXPOSE 80  
CMD ["/bin/bash", "/start.sh"]  
  

