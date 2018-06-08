FROM alpine:3.4  
ENV php_conf /etc/php5/php.ini  
ENV fpm_conf /etc/php5/php-fpm.conf  
  
RUN apk add --no-cache bash \  
openssh-client \  
wget \  
nginx \  
supervisor \  
curl \  
git \  
diffutils \  
  
# PHP core  
php5-fpm \  
# Database drivers  
php5-pdo \  
php5-pdo_sqlite \  
php5-mysql \  
php5-pgsql \  
# Helpful extensions  
php5-mcrypt \  
php5-ctype \  
php5-zlib \  
php5-gd \  
php5-intl \  
php5-memcache \  
php5-xml \  
php5-xsl \  
php5-curl \  
php5-openssl \  
php5-iconv \  
php5-json \  
php5-phar \  
php5-dom \  
php5-apcu \  
  
&& \  
  
mkdir -p /etc/nginx && \  
mkdir -p /var/www/app/ && \  
mkdir -p /run/nginx && \  
mkdir -p /var/log/supervisor  
  
# Copy our supervisor config  
ADD conf/supervisord.conf /etc/supervisord.conf  
  
# Copy our nginx config  
RUN rm -Rf /etc/nginx/nginx.conf  
ADD conf/nginx.conf /etc/nginx/nginx.conf  
  
# Copy our php-fpm config  
RUN rm -Rf /etc/php5/php-fpm.conf  
ADD conf/php-fpm.conf /etc/php5/php-fpm.conf  
  
# Install mediawiki and make a docker volume so we don't lose our stuff  
ADD https://releases.wikimedia.org/mediawiki/1.27/mediawiki-1.27.0.tar.gz
mediawiki.tar.gz  
RUN tar zxf mediawiki.tar.gz && mv mediawiki-1.27.0 /var/www/mediawiki  
VOLUME ["/var/www/mediawiki"]  
  
# Expose the NGINX ports and set the entrypoint to run supervisor  
EXPOSE 443 80  
ENTRYPOINT ["/usr/bin/supervisord", "-nc", "/etc/supervisord.conf"]  

