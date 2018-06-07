FROM php:7.0-fpm  
  
MAINTAINER Andrew Sparrow <a.vorobyev@mildberry.com>  
  
#####################################  
# Non-Root User Mildberry:  
#####################################  
RUN groupadd -g 1000 mildberry && \  
useradd -u 1000 -g mildberry -m mildberry  
  
#####################################  
# APT-GET:  
#####################################  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \  
&& echo "deb http://nginx.org/packages/debian/ jessie nginx" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
ca-certificates \  
nginx \  
nginx-module-xslt \  
nginx-module-geoip \  
nginx-module-image-filter \  
nginx-module-perl \  
nginx-module-njs \  
gettext-base \  
libmemcached-dev \  
libz-dev \  
libpq-dev \  
libjpeg-dev \  
libpng12-dev \  
libfreetype6-dev \  
libssl-dev \  
libmcrypt-dev \  
libzmq-dev \  
libpq-dev \  
libmysqlclient-dev \  
nano \  
git \  
ssh \  
nodejs && \  
apt-get clean  
  
RUN docker-php-ext-install -j$(nproc) iconv mcrypt zip pdo pgsql pdo_pgsql
mysqli pdo_mysql \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& pecl install zmq-beta \  
&& docker-php-ext-enable zmq \  
&& npm config set registry http://registry.npmjs.org/ \  
&& curl https://getcomposer.org/composer.phar > /usr/local/bin/composer \  
&& chmod +x /usr/local/bin/composer  
  
#####################################  
# xDebug:  
#####################################  
ARG INSTALL_XDEBUG=true  
ENV INSTALL_XDEBUG ${INSTALL_XDEBUG}  
RUN if [ ${INSTALL_XDEBUG} = true ]; then \  
pecl install xdebug && \  
docker-php-ext-enable xdebug \  
;fi  
  
ARG XDEBUG_REMOTE_HOST=""  
ENV XDEBUG_REMOTE_HOST ${XDEBUG_REMOTE_HOST}  
  
###################################  
# App files:  
#####################################  
WORKDIR /var/www/  
ADD . /var/www/  
RUN rm -rf /var/www/container  
  
######################################  
## Container files:  
######################################  
ADD ./container /container  
  
#####################################  
# RSA ssh  
#####################################  
ADD ./container/rsa/ /root/.ssh/  
RUN cp /container/rsa/* /root/.ssh/ && \  
chmod 600 /root/.ssh/id_rsa && \  
echo "Host bitbucket.com\n\tStrictHostKeyChecking no\n" >> /root/.ssh/config  
  
#####################################  
# PHP-FPM conf  
#####################################  
RUN php /container/templates/php.ini.php > /usr/local/etc/php/conf.d/php.ini
&& \  
rm /usr/local/etc/php-fpm.d/www.conf && \  
cp /container/config/php.pool.conf /usr/local/etc/php-fpm.d/php.pool.conf  
  
#####################################  
# NGINX conf  
#####################################  
RUN cp /container/config/nginx.conf /etc/nginx/nginx.conf && \  
cp /container/config/server_defaults.conf /etc/nginx/server_defaults.conf && \  
cp /container/config/laravel.conf /etc/nginx/conf.d/laravel.conf && \  
rm /etc/nginx/conf.d/default.conf  
  
#####################################  
# Webpack install:  
#####################################  
ARG INSTALL_WEBPACK=false  
ENV INSTALL_WEBPACK ${INSTALL_WEBPACK}  
RUN if [ ${INSTALL_WEBPACK} = true ]; then \  
npm install webpack -g \  
;fi  
  
#####################################  
# Frontend building  
#####################################  
ARG FRONTEND_VERSION="v0.0.22.1"  
ENV FRONTEND_VERSION ${FRONTEND_VERSION}  
ARG FRONTEND_LANG="zh"  
ENV FRONTEND_LANG ${FRONTEND_LANG}  
ARG BUILD_FRONTEND=true  
ENV BUILD_FRONTEND ${BUILD_FRONTEND}  
RUN if [ ${BUILD_FRONTEND} = true ]; then \  
cd /var/www/resources && \  
npm install && \  
webpack && \  
rm -rf /var/www/resources/src && \  
rm -rf /var/www/resources/node_modules && \  
rm /var/www/resources/webpack.config.js && \  
mkdir /var/www/resources/frontend && \  
cd /var/www/resources/frontend && \  
git clone git@bitbucket.org:treesoftrussia/frontend.git ./ && \  
git fetch --tags && \  
git checkout tags/${FRONTEND_VERSION} && \  
echo "{\"locale\": \"${FRONTEND_LANG}\"}" > ./build-config.json && \  
npm install && \  
chmod -R 755 /var/www/resources/frontend/node_modules && \  
npm run build && \  
cp -a /var/www/resources/frontend/dist/. /var/www/public && \  
rm -rf /var/www/resources/frontend \  
;fi  
  
RUN ln -sf /var/www/storage/app/public /var/www/public/storage && \  
cd /var/www  
  
#####################################  
# Composer install  
#####################################  
ARG COMPOSER_INSTALL_RUN=true  
ENV COMPOSER_INSTALL_RUN ${COMPOSER_INSTALL_RUN}  
RUN if [ ${COMPOSER_INSTALL_RUN} = true ]; then \  
composer install && composer dump-autoload \  
;fi  
  
#####################################  
# Webpack uninstall:  
#####################################  
RUN if [ ${INSTALL_WEBPACK} = false ]; then \  
npm uninstall webpack -g \  
;fi  
  
#####################################  
# App files permissions & Clean up and ready to go:  
#####################################  
RUN find ./ -type d -exec chmod 755 {} + && \  
find ./ -type f -exec chmod 644 {} + && \  
chmod -R ug+rwx ./storage && \  
chown -R mildberry:mildberry ./ && \  
chmod 700 /var/www/bin/run.sh && \  
rm -rf /container  
  
EXPOSE 80 443  
  
ENTRYPOINT ["./bin/run.sh"]  

