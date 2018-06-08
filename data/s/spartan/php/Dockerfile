FROM debian:jessie  
MAINTAINER Daniel Paul Searles <daniel.paul.searles@gmail.com>  
  
ENV APP_ENVIRONMENT=production  
  
ENTRYPOINT ["/usr/local/bin/entrypoint"]  
  
COPY entrypoint /usr/local/bin/  
  
RUN apt-get update && \  
apt-get install -y \  
git \  
php5 \  
php5-apcu \  
php5-cgi \  
php5-cli \  
php5-common \  
php5-curl \  
php5-fpm \  
php5-gd \  
php5-intl \  
php5-json \  
php5-mcrypt \  
php5-mysqlnd \  
php5-xdebug  
  
# Remove xdebug from enabled plugins. It can be re-enabled in with an  
# environment ini  
RUN rm $(find /etc/php5 -type l -name "*xdebug.ini");  
  
RUN php -r "readfile('https://getcomposer.org/installer');" \  
| php -- --install-dir=/usr/local/bin --filename=composer  
  
ONBUILD COPY php.custom.conf.d /etc/php5/custom.conf.d  

