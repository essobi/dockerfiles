FROM ubuntu:trusty  
  
MAINTAINER Patrick Nazar <patricknazar@internode.on.net>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -y install apache2 libapache2-mod-php5 php5-mysql php-apc php5-mcrypt
php5-curl && \  
echo "ServerName localhost" >> /etc/apache2/apache2.conf  
  
ADD apache_default /etc/apache2/sites-available/000-default.conf  
RUN a2enmod rewrite expires  
  
ENV PHP_UPLOAD_MAX_FILESIZE 10M  
ENV PHP_POST_MAX_SIZE 10M  
ENV PHP_SHORT_OPEN_TAG On  
ENV PHP_MEMORY_LIMIT 256M  
  
VOLUME ["/var/www/html"]  
  
COPY apache2-foreground /usr/local/bin/  
  
RUN touch /test  
  
RUN sed -i 's/upload_max_filesize = .*/upload_max_filesize =
'${PHP_UPLOAD_MAX_FILESIZE}'/' /etc/php5/apache2/php.ini && \  
sed -i 's/post_max_size = .*/post_max_size = '${PHP_POST_MAX_SIZE}'/'
/etc/php5/apache2/php.ini && \  
sed -i 's/short_open_tag = .*/short_open_tag = '${PHP_SHORT_OPEN_TAG}'/'
/etc/php5/apache2/php.ini && \  
sed -i 's/memory_limit = .*/memory_limit = '${PHP_MEMORY_LIMIT}'/'
/etc/php5/apache2/php.ini  
  
EXPOSE 80  
CMD ["apache2-foreground"]  

