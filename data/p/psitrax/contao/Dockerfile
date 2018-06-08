FROM centos:7  
MAINTAINER Christoph Wiechert <wio@psitrax.de>  
ENV REFRESHED_AT="2018-03-27"  
ENV TIMEZONE="Europe/Berlin" \  
RUN_ID="" \  
XDEBUG="false" \  
PHP_VALUE="" \  
PHP_ADMIN_VALUE=""  
  
RUN yum install epel-release -y \  
&& yum -y install https://centos7.iuscommunity.org/ius-release.rpm \  
&& yum upgrade -y \  
&& yum install -y \  
git \  
less \  
vim \  
wget \  
net-tools \  
locales \  
sendmail \  
openssl \  
ca-certificates \  
bzip2 \  
httpd \  
php72u-bcmath \  
php72u-cli \  
php72u-fpm \  
php72u-fpm-httpd \  
php72u-gd \  
php72u-pecl-imagick \  
php72u-intl \  
php72u-json \  
php72u-mbstring \  
php72u-mcryp \  
php72u-mysqlnd \  
php72u-snmp \  
php72u-soap \  
php72u-xml \  
php72u-pecl-xdebug \  
&& wget https://getcomposer.org/download/1.6.4/composer.phar -O
/usr/bin/composer \  
&& chmod +x /usr/bin/composer \  
&& rm -rf /var/www/* \  
&& chsh -s /bin/bash apache \  
&& yum clean all  
  
ADD rootfs /  
RUN chown apache /usr/share/httpd  
  
EXPOSE 80  
VOLUME ["/var/www"]  
WORKDIR /var/www  
HEALTHCHECK CMD curl -f http://localhost/ || exit 1  
  
CMD ["/init"]  
  

