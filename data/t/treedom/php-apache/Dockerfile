FROM ubuntu:trusty  
  
MAINTAINER Giacomo Triggiano <gtriggiano@treedom.net>  
  
ENV TIMEZONE Europe/Rome  
ENV PHP_MEMORY_LIMIT 512M  
ENV MAX_UPLOAD 50M  
ENV PHP_MAX_FILE_UPLOAD 200  
ENV PHP_MAX_POST 100M  
ENV ALLOW_OVERRIDE @false@  
ENV DOC_ROOT @false@  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -yq install \  
curl \  
apache2 \  
libapache2-mod-php5 \  
php5-mysql \  
php5-mcrypt \  
php5-gd \  
php5-curl \  
php5-apcu \  
php-pear \  
unzip \  
zip && \  
/usr/sbin/php5enmod mcrypt && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
mkdir -p /app && rm -fr /var/www/html && ln -s /app /var/www/html  
  
ADD run.sh /run.sh  
  
RUN chmod 755 /*.sh  
  
EXPOSE 80  
WORKDIR /app  
  
CMD ["/run.sh"]  

