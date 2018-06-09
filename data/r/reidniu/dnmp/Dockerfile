FROM alpine:3.4  
  
MAINTAINER ngineered <reid.niu@gmail.com>  
  
RUN echo http://nl.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories && \  
apk update && \  
apk add bash \  
openssh-client \  
wget \  
git \  
nginx \  
curl \  
openrc \  
ca-certificates \  
mysql \  
mysql-client \  
php5-fpm \  
php5-pdo \  
php5-pdo_mysql \  
php5-mysqli \  
php5-mcrypt \  
php5-ctype \  
php5-zlib \  
php5-gd \  
php5-intl \  
php5-memcached \  
php5-pdo_pgsql \  
php5-pgsql \  
php5-xml \  
php5-xsl \  
php5-curl \  
php5-openssl \  
php5-iconv \  
php5-json \  
php5-phar \  
php5-soap \  
php5-dom && \  
apk add -u musl && \  
mkdir -p /var/lib/mysql && \  
mkdir -p /etc/mysql/conf.d && \  
mkdir -p /var/run/mysql/ && \  
mkdir -p /etc/nginx/conf.d && \  
mkdir -p /run/nginx && \  
mkdir -p /root/.ssh && \  
curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer && \  
rm -rf /var/cache/apk/*  
  
ADD conf/default.conf /  
ADD conf/nginx.conf /etc/nginx/  
ADD conf/my.cnf /etc/mysql/  
ADD conf/php-fpm.conf /etc/php/  
ADD conf/run.sh /  
RUN chmod +x /run.sh  
  
EXPOSE 80 443 3306  
WORKDIR /web/www  
VOLUME ["/web/www", "/etc/nginx/conf.d", "/web/logs", "/var/lib/mysql",
"/etc/mysql/conf.d/", "/root/.ssh"]  
CMD ["/run.sh"]

