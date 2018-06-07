FROM ubuntu:trusty  
MAINTAINER Jagdeep Singh Banga <jagdeepsingh@whitelabelled.com>  
  
# Install base packages  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -yq install \  
curl \  
apache2 \  
libapache2-mod-php5 \  
php5-mysql \  
php5-gd \  
php5-curl \  
php5-mcrypt \  
mysql-client-core-5.6 \  
php-pear \  
php-apc && \  
rm -rf /var/lib/apt/lists/* && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf && \  
sed -i "s/variables_order.*/variables_order = \"EGPCS\"/g"
/etc/php5/apache2/php.ini  
  
RUN php5enmod mcrypt  
  
# Add image configuration and scripts  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
  
EXPOSE 80  
WORKDIR /var/www/html  
CMD ["/run.sh"]

