FROM laradock/php-fpm:7.0\--1.0  
MAINTAINER "Andrew McLagan" <andrew@ethicaljobs.com.au>  
  
#  
#--------------------------------------------------------------------------  
# HHVM source (copied from official)  
#--------------------------------------------------------------------------  
#  
ENV HHVM_VERSION need-to-add-versioning  
  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0x5a16e7281be7a449 && \  
echo deb http://dl.hhvm.com/debian jessie main | tee
/etc/apt/sources.list.d/hhvm.list  
  
#  
#--------------------------------------------------------------------------  
# Nginx (copied from official)  
#--------------------------------------------------------------------------  
#  
ARG NGINX_VERSION=1.10.1-1~jessie  
ENV NGINX_VERSION ${NGINX_VERSION}  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \  
&& echo "deb http://nginx.org/packages/debian/ jessie nginx" >>
/etc/apt/sources.list  
  
#  
#--------------------------------------------------------------------------  
# XDebug (optional)  
#--------------------------------------------------------------------------  
#  
ARG INSTALL_XDEBUG=false  
ENV INSTALL_XDEBUG ${INSTALL_XDEBUG}  
RUN if [ ${INSTALL_XDEBUG} = true ]; then \  
pecl install xdebug && \  
docker-php-ext-enable xdebug \  
;fi  
  
#  
#--------------------------------------------------------------------------  
# Mongo (optional)  
#--------------------------------------------------------------------------  
#  
ARG INSTALL_MONGO=true  
ENV INSTALL_MONGO ${INSTALL_MONGO}  
RUN if [ ${INSTALL_MONGO} = true ]; then \  
pecl install mongodb \  
;fi  
  
#  
#--------------------------------------------------------------------------  
# Install it all.  
#--------------------------------------------------------------------------  
#  
RUN apt-get update && apt-get install --no-install-recommends --no-install-
suggests -y \  
ca-certificates \  
nginx=${NGINX_VERSION} \  
nginx-module-xslt \  
nginx-module-geoip \  
nginx-module-image-filter \  
nginx-module-perl \  
nginx-module-njs \  
gettext-base \  
hhvm \  
supervisor \  
git \  
wget \  
zip \  
unzip \  
&& apt-get clean  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
#  
#--------------------------------------------------------------------------  
# Tools: PHPUnit, Composer, Prestissimo, Laravel 5.x.x (composer caching)  
#--------------------------------------------------------------------------  
#  
RUN cd $HOME && \  
wget http://getcomposer.org/composer.phar && \  
chmod +x composer.phar && \  
mv composer.phar /usr/local/bin/composer && \  
wget https://phar.phpunit.de/phpunit.phar && \  
chmod +x phpunit.phar && \  
mv phpunit.phar /usr/local/bin/phpunit && \  
composer global require hirak/prestissimo && \  
composer global require laravel/framework:5.*  
  
#  
#--------------------------------------------------------------------------  
# Configs  
#--------------------------------------------------------------------------  
#  
ADD ./config/nginx.conf /etc/nginx  
  
ADD ./config/php.ini /usr/local/etc/php/conf.d  
  
ADD ./config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
#  
#--------------------------------------------------------------------------  
# Source  
#--------------------------------------------------------------------------  
#  
RUN mkdir -p /var/www  
  
ADD ./index.php /var/www/public/index.php  
  
WORKDIR /var/www  
  
#  
#--------------------------------------------------------------------------  
# Init  
#--------------------------------------------------------------------------  
#  
COPY ./index.php /var/www/public/index.php  
  
RUN usermod -u 1000 www-data  
  
CMD ["/usr/bin/supervisord"]  
  
EXPOSE 80 443  

