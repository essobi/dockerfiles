FROM ubuntu:14.04  
MAINTAINER Jerome Schaeffer <j.schaeffer@flash-global.net>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV APP_ENV dev  
  
RUN apt-get -qq update && \  
apt-get install -y apache2 libapache2-mod-php5 \  
php5-mysqlnd php5-xmlrpc php-soap php5-mcrypt php5-curl \  
php5-gd php5-xdebug mysql-client \  
pdftk a2ps ghostscript htmldoc ssh \  
php5-memcache \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY config/000-default.conf /etc/apache2/sites-available/000-default.conf  
COPY config/php.ini /etc/php5/apache2/php.ini  
COPY config/mime.conf /etc/apache2/mods-available/mime.conf  
COPY config/xdebug.ini /etc/php5/mods-available/xdebug.ini  
  
#Symlinks for PDF executable  
RUN ln -s /usr/bin/psjoin /usr/local/bin/psjoin \  
&& ln -s /usr/bin/gs /usr/local/bin/gs \  
&& ln -s /usr/bin/php /usr/local/bin/php  
  
RUN a2enmod rewrite  
  
#Create necessary folders  
RUN mkdir -p /var/www/intranet/BROUILLONS \  
&& chmod 777 /var/www/intranet/BROUILLONS \  
&& mkdir /NASTEMPO \  
&& chmod 777 /NASTEMPO  
  
EXPOSE 80  
ADD start.sh /start.sh  
RUN chmod 0755 /start.sh  
CMD ["bash", "start.sh"]

