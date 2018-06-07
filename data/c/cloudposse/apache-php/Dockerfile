FROM cloudposse/apache  
MAINTAINER Erik Osterman "e@osterman.com"  
USER root  
  
  
# Install Apache with PHP 5.5  
RUN echo 'deb http://repo.suhosin.org/ ubuntu-trusty main' >>
/etc/apt/sources.list && \  
wget -q https://sektioneins.de/files/repository.asc -O - | apt-key add - && \  
apt-get update && \  
apt-get install -y libapache2-modsecurity \  
libapache2-mod-php5 \  
apache2-mpm-prefork \  
php5-cli \  
php5 \  
php-mail \  
php5-json \  
php5-readline \  
php5-redis \  
php5-memcache \  
php5-apcu \  
php5-mcrypt \  
php5-curl \  
php5-gd \  
php5-pgsql \  
php5-mysql \  
php5-suhosin-extension && \  
apt-get clean && rm -rf /tmp/* /var/tmp/*  
  
ADD modsecurity/ /etc/modsecurity/  
ADD php-mods-available/ /etc/php5/mods-available/  
ADD mods-available /etc/apache2/mods-available/  
ADD conf-available /etc/apache2/conf-available/  
ADD start /start  
  
RUN php5enmod suhosin && \  
php5enmod security && \  
php5enmod short-open-tag && \  
php5enmod uploads && \  
a2enmod mpm_prefork && \  
a2enmod security2 && \  
a2enmod php5  
  

