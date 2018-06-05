# VERSION 1  
FROM centos  
  
MAINTAINER webts  
  
# update centos  
RUN yum -y update  
  
# install required  
RUN yum install -y httpd php-devel wget php-pear unzip gcc-c++  
  
#install mongo drivers  
RUN pecl install mongo  
RUN cd /etc && echo "extension=mongo.so" >> php.ini  
  
# install RockMongo  
RUN cd /root && wget http://rockmongo.com/downloads/go?id=12 && unzip
rockmongo-1.1.5.zip -d /var/www/ && rm -R /var/www/html && mv
/var/www/rockmongo/ /var/www/html  
RUN sed -i 's/"Localhost"/getenv('DB_NAME')/g' /var/www/html/config.php  
RUN sed -i 's/"127.0.0.1"/getenv('DB_PORT_27017_TCP_ADDR')/g'
/var/www/html/config.php  
  
# increase php upload size  
RUN sed -i 's/upload_max_filesize = 2M/upload_max_filesize = 10M/g'
/etc/php.ini  
RUN sed -i 's/post_max_size = 2M/post_max_size = 10M/g' /etc/php.ini  
  
#RUN echo '<?php phpInfo(); ?>' > /var/www/html/info.php  
ENTRYPOINT ["/usr/sbin/httpd"]  
CMD ["-D", "FOREGROUND"]

