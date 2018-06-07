######################################################  
#  
# PHP 5.6 Base Image  
# Tag: deardooley/php:5.6  
#  
# This is a minimal alpine-based php 5.6 image with Apache 2.4.  
#  
######################################################  
  
FROM deardooley/httpd:2.4  
MAINTAINER Rion Dooley <dooley@tacc.utexas.edu  
  
RUN echo http://alpine.gliderlabs.com/alpine/edge/main >>
/etc/apk/repositories && \  
echo http://alpine.gliderlabs.com/alpine/edge/community >>
/etc/apk/repositories && \  
apk-install curl zip php5-apache2 php5-cli php5-curl php5-gd php5-json
php5-phar php5-openssl php5-mysql php5-pdo php5-zip php5-ctype php5-mysqli
php5-iconv php5-zlib php5-xml php5-dom php5-mcrypt php5-pdo_mysql php5-pcntl
php5-posix ssmtp  
  
RUN apk-install shadow --repository
http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted && \  
apk-install php5-redis --repository
http://nl.alpinelinux.org/alpine/edge/testing \--allow-untrusted && \  
rm -f /var/cache/apk/* && \  
# fix the apache user uid to line up with system user namespace  
usermod -u 1000 apache && \  
groupmod -g 50 apache && \  
mkdir -p /var/lib/php/session && \  
chown -R apache:root /var/lib/php/session && \  
# Updating apache defaults for php  
sed -i 's#DirectoryIndex index.html#DirectoryIndex index.php index.html#'
/etc/apache2/httpd.conf && \  
rm -f /var/www/html/index.html && \  
  
# create default php settings  
echo "<?php phpinfo(); ?>" > /var/www/html/index.php && \  
chown -R apache:apache /var/www/html && \  
  
# configure ssmtp to read from env so php's mail() function will work out of
the box.  
sed -ri -e 's/^(mailhub=).*/\1%%SMTP_HUB%%/' -e 's/^#(FromLineOverride)/\1/'
/etc/ssmtp/ssmtp.conf && \  
echo "AuthUser=%%SMTP_USER%%" >> /etc/ssmtp/ssmtp.conf && \  
echo "AuthPass=%%SMTP_PASSWORD%%" >> /etc/ssmtp/ssmtp.conf && \  
echo "UseSTARTTLS=YES" >> /etc/ssmtp/ssmtp.conf  
  
ADD php/php.ini /etc/php5/php.ini  

