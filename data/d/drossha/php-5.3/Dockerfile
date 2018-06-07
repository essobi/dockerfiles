FROM centos:centos6  
  
ENV PHP_VERSION 5.3.3  
ENV DIR $HOME  
ENV TIMEZONE Europe/Amsterdam  
  
RUN yum -y install epel-release  
  
RUN yum -y install pca-certificates \  
unzip \  
tar \  
git \  
which \  
mysql \  
patch \  
curl \  
wget \  
php-$PHP_VERSION \  
php-cli-$PHP_VERSION \  
php-common-$PHP_VERSION \  
php-fpm-$PHP_VERSION \  
php-intl-$PHP_VERSION \  
php-mbstring-$PHP_VERSION \  
php-mcrypt-$PHP_VERSION \  
php-pdo-$PHP_VERSION \  
php-pear \  
php-gd \  
php-pecl-apc \  
php-pecl-igbinary \  
php-pecl-memcache \  
php-pecl-redis \  
php-pecl-geoip \  
php-pgsql-$PHP_VERSION \  
php-redis \  
php-soap-$PHP_VERSION \  
php-xml-$PHP_VERSION \  
php-mysql \  
php-mysqli \  
php-redis  
  
RUN yum clean all  
  
#  
# configuracion de php.ini  
#  
RUN mkdir -p /data/etc/php  
  
RUN rm /etc/php.d -Rf  
RUN rm /etc/php.ini -Rf  
#---------------------------  
#  
#---------------------------  
ADD etc /etc  
ADD gitconfig /root/.gitconfig  
RUN sed -i $(echo "s/{TIMEZONE}/$(echo $TIMEZONE | sed -e 's/\//\\\\\//g')/g")
/etc/php.d/date.ini  
RUN ln -sf /usr/share/zoneinfo/$TIMEZONE /etc/localtime  
  
WORKDIR /data  
EXPOSE 9000  
ENTRYPOINT exec php-fpm --fpm-config /etc/php-fpm.d/www.conf -RF

