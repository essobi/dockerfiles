# Akeneo  
FROM ubuntu:trusty  
MAINTAINER Vincent ARROCENA <varrocen@gmail.com>  
  
# Install Apache and PHP  
RUN apt-get update \  
&& apt-get install -y apache2 \  
libapache2-mod-php5 \  
php5-cli \  
php5-mysql \  
php5-intl \  
php5-curl \  
php5-gd \  
php5-mcrypt \  
php5-apcu \  
php5-mongo \  
curl \  
&& php5enmod mcrypt \  
&& a2enmod rewrite \  
&& rm -r /var/lib/apt/lists/*  
  
# Setting up PHP configuration  
RUN sed -i 's/memory_limit = 128M/memory_limit = 512M/'
/etc/php5/apache2/php.ini \  
&& sed -i 's/;date.timezone =/date.timezone = Europe\/Paris/'
/etc/php5/apache2/php.ini \  
&& sed -i 's/memory_limit = -1/memory_limit = 768M/' /etc/php5/cli/php.ini \  
&& sed -i 's/;date.timezone =/date.timezone = Europe\/Paris/'
/etc/php5/cli/php.ini  
  
# Installing Akeneo PIM  
COPY akeneo-pim.local.conf /etc/apache2/sites-available/  
RUN curl -SL http://www.akeneo.com/pim-community-standard-v1.3-latest-
icecat.tar.gz \  
| tar -zxC /var/www \  
&& a2ensite akeneo-pim.local \  
&& a2dissite 000-default  
  
# Initializing Akeneo  
COPY init-akeneo.sh /init-akeneo.sh  
RUN chmod +x init-akeneo.sh  
  
EXPOSE 80  
VOLUME ["/var/www", "/var/log/apache2"]  
ENTRYPOINT ["/init-akeneo.sh"]  

