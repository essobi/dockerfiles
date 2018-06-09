FROM ubuntu:16.04  
MAINTAINER Bruce McCleave<bruce@thinkiq.com>  
  
USER root  
  
COPY docker-startup.sh /usr/local/bin/docker-startup.sh  
RUN apt-get -o Acquire::ForceIPv4=true update && \  
apt-get install -y && \  
apt-get -o Acquire::ForceIPv4=true upgrade -y && \  
apt-get -o Acquire::ForceIPv4=true -y install software-properties-common && \  
apt-get -o Acquire::ForceIPv4=true update && \  
apt-get -o Acquire::ForceIPv4=true install -y sudo \  
curl \  
tar \  
openssl \  
rsync \  
vim \  
bash-completion \  
unzip \  
php \  
wget \  
tzdata \  
nginx \  
php-fpm\  
php-cli \  
php-phar \  
php-zip \  
php-bz2 \  
php-ctype \  
php-mysqli \  
php-mysql \  
php-pdo \  
php-json \  
php-curl \  
php-gd \  
php-gmp \  
php-mcrypt \  
php-dom \  
php-xml \  
php-iconv \  
php-dev \  
php-gd \  
php-memcache \  
php-pspell \  
php-snmp \  
snmp \  
php-xmlrpc \  
supervisor && \  
echo "#disable ipv6" | sudo tee -a /etc/sysctl.conf && \  
echo "net.ipv6.conf.all.disable_ipv6 = 1" | sudo tee -a /etc/sysctl.conf && \  
echo "net.ipv6.conf.default.disable_ipv6 = 1" | sudo tee -a /etc/sysctl.conf
&& \  
echo "net.ipv6.conf.lo.disable_ipv6 = 1" | sudo tee -a /etc/sysctl.conf && \  
sysctl -p && \  
echo "cgi.fix_pathinfo=0" >> /etc/php/7.0/fpm/php.ini && \  
chmod 777 /var/www/html && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
chmod 755 /usr/local/bin/docker-startup.sh  
  
COPY default.conf /etc/nginx/sites-available/default  
  
EXPOSE 80 443

