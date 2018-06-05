FROM ubuntu:16.04  
MAINTAINER Jaouher Kharrat<kharrat_jaouher@hotmail.fr>  
  
# Build-time metadata as defined at http://label-schema.org  
ARG BUILD_DATE=04-12-2017  
ARG VCS_REF=R1v2  
ARG VERSION=1.0  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="docker ubuntu16 lamp-xdebug ssl phpunit " \  
org.label-schema.description="Basic ubuntu16 installation along with apache,
mysql and PHP7 Added modules are Xdebug-SSL-PHPUnit" \  
org.label-schema.url="https://github.com/JaouherK/docker-ubuntu16-lamp-xdebug-
ssl-phpunit/edit/master/Dockerfile" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/JaouherK/docker-ubuntu16-lamp-
xdebug-ssl-phpunit/edit/master/Dockerfile" \  
org.label-schema.vendor="Shinigami" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
  
## ***********************************************************************  
# Server update and basic install tools  
## ***********************************************************************  
RUN apt-get update && \  
apt-get install -y wget \  
curl \  
software-properties-common \  
python3-software-properties \  
python-software-properties \  
unzip \  
vim \  
bash-completion \  
apache2  
  
## ***********************************************************************  
# Apache  
## ***********************************************************************  
RUN apt-get install -y apache2  
RUN service apache2 restart  
  
## ***********************************************************************  
# PHP / Mysql and relative modules  
## ***********************************************************************  
RUN locale -a  
RUN export LANG=C.UTF-8 && \  
add-apt-repository ppa:ondrej/php && \  
apt-get update  
  
RUN apt-get install -y libapache2-mod-php7.0 \  
libzend-framework-php \  
php7.0 \  
php7.0-bcmath \  
php7.0-bz2 \  
php7.0-cgi \  
php7.0-common \  
php7.0-curl \  
php7.0-fpm \  
php7.0-gd \  
php7.0-gmp \  
php-http \  
php-imagick \  
php7.0-imap \  
php7.0-intl \  
php7.0-json \  
php7.0-ldap \  
php7.0-mbstring \  
php7.0-mcrypt \  
php-memcache \  
php-memcached \  
php7.0-mysql \  
php7.0-recode \  
php7.0-soap \  
php-xdebug \  
php7.0-xml \  
php7.0-xsl \  
php7.0-zip \  
## To install mysql while forcing the user to root and password to empty  
&& { \  
echo debconf debconf/frontend select Noninteractive; \  
echo mysql-community-server mysql-community-server/data-dir \  
select ''; \  
echo mysql-community-server mysql-community-server/root-pass \  
password 'JohnUskglass'; \  
echo mysql-community-server mysql-community-server/re-root-pass \  
password 'JohnUskglass'; \  
echo mysql-community-server mysql-community-server/remove-test-db \  
select true; \  
} | debconf-set-selections \  
&& apt-get install -y mysql-server \  
python \  
python-django \  
python-celery \  
rabbitmq-server \  
git\  
mysql-client  
  
## ***********************************************************************  
## configure PHP  
## ***********************************************************************  
RUN ["bin/bash", "-c", "sed -i
's/max_execution_time\\\s*=.*/max_execution_time=180/g'
/etc/php/7*/apache2/php.ini"]  
RUN ["bin/bash", "-c", "sed -i
's/upload_max_filesize\\\s*=.*/upload_max_filesize=16M/g'
/etc/php/7*/apache2/php.ini"]  
RUN ["bin/bash", "-c", "sed -i 's/memory_limit\\\s*=.*/memory_limit=256M/g'
/etc/php/7*/apache2/php.ini"]  
RUN ["bin/bash", "-c", "sed -i 's/post_max_size\\\s*=.*/post_max_size=20M/g'
/etc/php/7*/apache2/php.ini"]  
  
## ***********************************************************************  
## configure XDebug  
## ***********************************************************************  
RUN ["bin/bash", "-c", "echo [XDebug] >> /etc/php/7*/apache2/php.ini"]  
RUN ["bin/bash", "-c", "echo xdebug.remote_autostart=1 >>
/etc/php/7*/apache2/php.ini"]  
RUN ["bin/bash", "-c", "echo xdebug.remote_enable=1 >>
/etc/php/7*/apache2/php.ini"]  
RUN ["bin/bash", "-c", "echo xdebug.remote_connect_back=1 >>
/etc/php/7*/apache2/php.ini"]  
RUN ["bin/bash", "-c", "echo xdebug.idekey=netbeans-xdebug >>
/etc/php/7*/apache2/php.ini"]  
  
## ***********************************************************************  
## configure Apache  
## ***********************************************************************  
# Apache mod rewrite  
RUN a2enmod rewrite  
  
# Apache SSL install and init  
RUN apt-get install -y openssl \  
&& a2enmod ssl \  
&& mkdir /etc/apache2/ssl \  
&& openssl req -new -x509 -days 365 -sha1 -newkey rsa:1024 -nodes -keyout
/etc/apache2/ssl/server.key -out /etc/apache2/ssl/server.crt -subj
'/O=Company/OU=Department/CN=localhost'  
  
# Apache SSL install and init  
COPY config/default.conf /etc/apache2/sites-available/000-default.conf  
  
RUN wget https://phar.phpunit.de/phpunit-3.7.38.phar -O phpunit.phar \  
&& chmod +x phpunit.phar \  
&& mv phpunit.phar /usr/share/php/phpunit  
  
RUN service apache2 restart  
RUN service mysql start  
  
## ***********************************************************************  
## Copy data to the server if existenet data base / website  
## ***********************************************************************  
##  
## COPY db.sql /db.sql  
## COPY website /var/www/html  
EXPOSE 80 443  
WORKDIR /var/www/html  
  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

