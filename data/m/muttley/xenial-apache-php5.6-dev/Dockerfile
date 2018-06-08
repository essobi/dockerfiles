FROM ubuntu:xenial  
  
# Set correct environment variables.  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
  
RUN locale-gen en_US.UTF-8 fr_CA.UTF-8  
ENV LANG en_US.UTF-8  
RUN echo "Europe/Rome" > /etc/timezone && dpkg-reconfigure tzdata  
  
RUN groupadd -g 600 webmgr  
RUN useradd -u 600 -g 600 webmgr  
  
RUN apt-get update  
RUN apt-get upgrade -y  
run apt-get -y install software-properties-common vim  
  
RUN add-apt-repository -y ppa:ondrej/php  
RUN apt-get update  
  
run apt-get -y install php5.6 \  
php5.6-mbstring \  
php5.6-mcrypt \  
php5.6-xml \  
php5.6-bcmath \  
php5.6-cli \  
php5.6-common \  
php5.6-curl \  
php5.6-dev \  
php5.6-gd \  
php5.6-intl \  
php5.6-json \  
php5.6-sqlite3 \  
php5.6-zip \  
php5.6-mysql \  
php-geoip \  
git \  
apache2 \  
libapache2-mod-php5.6 \  
supervisor \  
openssl \  
libssl-dev \  
libsslcommon2-dev  
  
run pecl install mongodb  
run echo "extension=mongodb.so" >> /etc/php/5.6/apache2/php.ini  
run sed -e 's/post_max_size = 8M/post_max_size = 100M/'
/etc/php/5.6/apache2/php.ini > /etc/php/5.6/apache2/php.ini  
run sed -e 's/upload_max_filesize = 2M/upload_max_filesize = 100M/'
/etc/php/5.6/apache2/php.ini > /etc/php/5.6/apache2/php.ini  
run a2enmod rewrite  
  
VOLUME /var/www/html  
VOLUME /etc/apache2  
VOLUME /etc/php/5.6/apache  
  
WORKDIR /var/www/html  
  
ENV APACHE_RUN_USER webmgr  
ENV APACHE_RUN_GROUP webmgr  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
  
RUN mkdir -p $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR
/var/log/supervisor  
  
COPY supervisor.conf /etc/supervisor/conf.d/supervisor.conf  
  
EXPOSE 80  
CMD ["service", "supervisor", "start"]  
  

