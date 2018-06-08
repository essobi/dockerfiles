FROM ubuntu:xenial  
MAINTAINER Enric Mieza <enric@enricmieza.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get install -y curl \  
apache2 \  
libapache2-mod-php \  
php-mysql \  
php-gd \  
php-mbstring \  
mysql-server && \  
apt-get clean && apt-get autoclean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/www/html/* && \  
curl -o /zenphoto.tgz
https://codeload.github.com/zenphoto/zenphoto/tar.gz/master && \  
sed -i "/upload_max_filesize/c\upload_max_filesize = 20M"
/etc/php/7.0/apache2/php.ini && \  
echo "<Directory /var/www>" >> /etc/apache2/sites-available/000-default.conf
&& \  
echo " AllowOverride All" >> /etc/apache2/sites-available/000-default.conf &&
\  
echo " Options -Indexes +FollowSymLinks" >> /etc/apache2/sites-
available/000-default.conf && \  
echo "</Directory>" >> /etc/apache2/sites-available/000-default.conf && \  
sed -i "/<\/VirtualHost>/d" /etc/apache2/sites-available/000-default.conf && \  
echo "</VirtualHost>" >> /etc/apache2/sites-available/000-default.conf  
  
ADD run.sh /run.sh  
RUN chmod 755 /run.sh  
  
EXPOSE 80  
  
VOLUME ["/var/lib/mysql"]  
  
CMD ["/bin/bash","/run.sh"]  

