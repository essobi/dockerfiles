FROM ubuntu:trusty  
MAINTAINER Andrei Manea <andrei@cloudhero.io>  
  
# Install base packages  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -yq install \  
curl \  
apache2 \  
libapache2-mod-php5 \  
php5-mysql \  
php5-gd \  
php5-curl \  
php-pear \  
php5-mongo \  
php5-memcached \  
php-apc && \  
rm -rf /var/lib/apt/lists/* && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
sed -i "s/variables_order.*/variables_order = \"EGPCS\"/g"
/etc/php5/apache2/php.ini  
  
RUN rm -rf /var/www/html && mkdir -p /var/lock/apache2 /var/run/apache2
/var/log/apache2 /var/www/html && chown -R www-data:www-data /var/lock/apache2
/var/run/apache2 /var/log/apache2 /var/www/html  
  
# Apache + PHP requires preforking Apache for best results  
RUN a2dismod mpm_event && a2enmod mpm_prefork  
  
RUN mv /etc/apache2/apache2.conf /etc/apache2/apache2.conf.dist && rm
/etc/apache2/conf-enabled/* /etc/apache2/sites-enabled/*  
COPY apache2.conf /etc/apache2/apache2.conf  
  
# Add image configuration and scripts  
ADD apache2-foreground.sh /apache2-foreground.sh  
RUN chmod 755 /*.sh  
  
# Add sample welcome page  
ADD sample/ /var/www/html/  
  
VOLUME /var/www/html  
WORKDIR /var/www/html  
  
EXPOSE 80  
CMD ["/apache2-foreground.sh"]  

