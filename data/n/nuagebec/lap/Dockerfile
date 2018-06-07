FROM nuagebec/ubuntu:16.04  
MAINTAINER David Tremblay <david@nuagebec.ca>  
  
#install php and apache  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get upgrade -y &&\  
apt-get -yq install \  
rsync \  
curl \  
apache2 \  
libapache2-mod-php \  
libapache2-mod-security2 \  
php-mysql \  
php-gd \  
php-curl \  
php-pear \  
php-mcrypt \  
php-mail \  
mysql-client \  
php-intl \  
php-zip \  
php-mbstring && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
ADD supervisor_apache.conf /etc/supervisor/conf.d/apache.conf  
ADD ./config/php.ini /etc/php/7.0/apache2/conf.d/php.ini  
ADD ./config/000-default.conf /etc/apache2/sites-available/000-default.conf  
  
RUN mv /etc/modsecurity/modsecurity.conf-recommended
/etc/modsecurity/modsecurity.conf  
  
#Activate php-mcrypt  
RUN phpenmod mcrypt  
  
#Activate opcache parameters are in ../config/php.ini  
RUN phpenmod opcache  
  
#Activate mod_rewrite  
RUN a2enmod rewrite  
  
#activate mod_expires  
RUN a2enmod expires  
  
#activate mod_headers  
RUN a2enmod headers  
  
# activate intl  
RUN phpenmod intl  
  
RUN echo "<?php phpinfo();" > /var/www/html/index.php  
  
# Add VOLUMEs to allow sharing logs and backup  
VOLUME ["/var/log/apache2", "/var/www/html"]  
  
EXPOSE 80 443  
CMD ["/data/run.sh"]  
  

