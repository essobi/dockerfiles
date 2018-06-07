# Ubuntu 14.04 with php 5.4 installed.  
FROM ubuntu:14.04  
MAINTAINER @sagarmankari  
  
  
  
RUN apt-get update && \  
apt-get -y install gcc mono-mcs && \  
rm -rf /var/lib/apt/lists/*  
  
# Set correct environment variables.  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
ENV INITRD No  
  
# Our user in the container  
USER root  
WORKDIR /root  
  
# Need to generate our locale.  
RUN locale-gen de_DE de_DE.UTF-8  
ENV LANG de_DE.UTF-8  
ENV LANGUAGE de_DE.UTF-8  
RUN apt-get update  
  
# Install and Test PHP  
RUN apt-get install --no-install-recommends -y \  
curl ca-certificates \  
php5-cli \  
php5-dev \  
php5-xdebug \  
php-apc \  
php5-json \  
php5-memcached php5-memcache \  
php5-mysql php5-pgsql \  
php5-sqlite php5-sybase php5-interbase php5-odbc \  
php5-mcrypt \  
php5-ldap \  
php5-gmp \  
php5-intl \  
php5-geoip \  
php5-imagick php5-gd \  
php5-imap \  
php5-curl \  
php5-svn \  
php5-ps \  
php5-ming \  
php5-enchant \  
php5-xsl \  
php5-xmlrpc \  
php5-tidy \  
php5-recode \  
php5-readline \  
php5-pspell \  
php-pear && \  
php --version && \  
php -m  
  
# Create directory for lemur installation  
RUN mkdir -p /dir/subdir  
  
# Make sure package is up to date  
RUN apt-get update  
RUN apt-get install zlib1g-dev libncurses5-dev  
  
# update and install g++  
RUN apt-get install gcc g++ mono-mcs  
  
# install make  
RUN apt-get install --reinstall make  
  
# install lemur  
WORKDIR /dir  
ADD
https://downloads.sourceforge.net/project/lemur/lemur/indri-5.4/indri-5.4.tar.gz?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Flemur%2Ffiles%2Flemur%2Findri-5.4%2F&ts=1509711165&use_mirror=ayera
/dir/indri-5.4.tar.gz  
RUN tar -xzf indri-5.4.tar.gz  
WORKDIR /dir/indri-5.4/  
WORKDIR /  
  
#install mysql  
ENV MYSQL_USER=mysql \  
MYSQL_DATA_DIR=/var/lib/mysql \  
MYSQL_RUN_DIR=/run/mysqld \  
MYSQL_LOG_DIR=/var/log/mysql  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server \  
&& rm -rf ${MYSQL_DATA_DIR} \  
&& rm -rf /var/lib/apt/lists/*  
RUN apt-get update && apt-get install mysql-server  
  
# Tidy up  
RUN apt-get -y autoremove && apt-get clean && apt-get autoclean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install composer  
RUN curl https://getcomposer.org/installer | php -- && mv composer.phar
/usr/local/bin/composer && chmod +x /usr/local/bin/composer  
  
# Allow mounting files  
VOLUME ["/root"]  
  
# PHP is our entry point  
CMD ["/usr/bin/php"]  

