FROM ubuntu:14.04  
# Variables Apache  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_USER_UID 0  
RUN apt-get update && apt-get install -y wget  
  
RUN echo "deb http://packages.dotdeb.org jessie all" >> /etc/apt/sources.list  
RUN echo "deb-src http://packages.dotdeb.org jessie all" >>
/etc/apt/sources.list  
  
RUN wget --no-check-certificate https://www.dotdeb.org/dotdeb.gpg  
RUN apt-key add dotdeb.gpg  
  
# Java, PHP && Apache  
RUN apt-get update && apt-get install -y \  
sudo \  
curl \  
git \  
locate \  
vim \  
acl \  
apache2 \  
apache2-utils \  
php5 \  
php5-dev \  
php5-cli \  
php5-xdebug \  
php5-intl \  
php5-curl \  
php5-apcu \  
php-pear \  
php5-gd \  
php5-mcrypt \  
libapache2-mod-php5 \  
php5-mysql  
  
RUN echo "Europe/Paris" > /etc/timezone && dpkg-reconfigure -f noninteractive
tzdata  
RUN echo 'alias ll="ls -lah --color=auto"' >> /etc/bash.bashrc  
  
# Config Apache  
RUN a2enmod rewrite \  
&& a2enmod php5 \  
&& rm -f /etc/apache2/sites-enabled/* \  
&& rm -f /etc/apache2/sites-available/* \  
&& rm -rf /var/www/*  
  
# Config PHP  
RUN php5enmod mcrypt \  
&& service apache2 restart  
  
# Alias sf  
RUN echo "alias sf='php bin/console'" >> /root/.bashrc  
  
EXPOSE 80  
WORKDIR /src  
  
CMD /usr/sbin/apache2 -D FOREGROUND  

