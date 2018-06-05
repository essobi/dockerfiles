FROM php:5-apache  
MAINTAINER Jetsada Machom jim@imjim.im  
  
RUN apt-get update && \  
apt-get install -y curl \  
postgresql-server-dev-all && \  
docker-php-ext-install mysqli \  
pgsql && \  
curl -L https://www.adminer.org/latest-en.php > index.php && \  
echo "upload_max_filesize = 2000M" >>
/usr/local/etc/php/conf.d/upload_large.ini && \  
echo "post_max_size = 2000M" >> /usr/local/etc/php/conf.d/upload_large.ini &&
\  
echo "memory_limit = -1" >> /usr/local/etc/php/conf.d/upload_large.ini && \  
echo "max_execution_time = 0" >> /usr/local/etc/php/conf.d/upload_large.ini &&
\  
apt-get remove -y postgresql-server-dev-all && \  
apt-get autoclean && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

