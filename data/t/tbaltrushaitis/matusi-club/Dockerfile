FROM php:5.6-apache  
  
MAINTAINER Tomas Baltrushaitis <tbaltrushaitis@gmail.com>  
  
ADD configs/SHOP_OPTIONS /tmp/SHOP_OPTIONS  
CMD ["source", "/tmp/SHOP_OPTIONS"]  
  
CMD export \  
DATE "$(date +"%Y%m%d%H%M%S")" \  
DATETIME "$(date "+%Y-%m-%d")_$(date "+%H-%M-%S")" \  
BACK_PATH "/opt/backup/${DB_NAME}/" \  
WWW_USER "www-data" \  
DIR_WEB "webroot" \  
DIR_ROOT "/var/www/html/${APP_NAME}" \  
SHOP_WEB "${DIR_ROOT}/${DIR_WEB}" \  
SHOP_LOG "${DIR_ROOT}/${APP_NAME}_setup_${DATETIME}.log" \  
GIT_REPO "https://github.com/PrestaShop/PrestaShop.git" \  
GIT_DIR "PrestaShop.git"  
# Avoid MySQL questions during installation  
#ENV DEBIAN_FRONTEND noninteractive  
#RUN ["echo", "mysql-server-5.6", "mysql-server/root_password password",
"${DB_PASS}", "|", "debconf-set-selections"]  
#RUN ["echo", "mysql-server-5.6", "mysql-server/root_password_again",
"password", "${DB_PASS}", "|", "debconf-set-selections"]  
  
CMD apt-get update \  
&& apt-get install -y \  
libmcrypt-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
libfreetype6-dev \  
libxml2-dev \  
libicu-dev \  
mysql-client \  
wget \  
unzip \  
curl \  
git \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
&& docker-php-ext-install iconv \  
intl \  
mcrypt \  
opcache \  
pdo \  
mysql \  
pdo_mysql \  
mbstring \  
soap \  
gd \  
zip  
  
# mysql-server \  
# nodejs \  
# npm \  
# */  
# Get composer  
CMD php -r "copy('https://getcomposer.org/installer', '/tmp/composer-
setup.php');" \  
&& php /tmp/composer-setup.php \  
\--no-ansi \  
\--install-dir=/usr/local/bin \  
\--filename=composer \  
&& rm -rf /tmp/composer-setup.php  
  
#COPY config_files/config.json /root/.composer/config.json  
#RUN composer global require hirak/prestissimo:^0.1 \  
# && composer install --prefer-dist --no-interaction --no-progress \  
# && rm -rf /var/www/html/app/cache/*  
# */  
# Get PrestaShop  
CMD git clone \  
\--depth=50 \  
\--branch=master \  
"${GIT_REPO}" \  
"/var/www/${GIT_DIR}"  
# && cd "${GIT_DIR}" \  
# && git checkout -l master \  
# && git pull origin master  
#COPY config_files/docker_updt_ps_domains.php /var/www/html/  
  
  
WORKDIR /var/www/  
USER ${WWW_USER}  
  
  
# Apache configuration RUN a2enmod rewrite  
CMD mkdir -p /var/www \  
&& chown -R "${WWW_USER}:${WWW_USER}" /var/www  
  
# PHP configuration  
#COPY config_files/php.ini /usr/local/etc/php/  
# MySQL configuration  
#RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf  
#EXPOSE 3306  
#VOLUME /var/www/html/modules  
#VOLUME /var/www/html/themes  
#VOLUME /var/www/html/override  
#COPY config_files/docker_run.sh /tmp/  
#CMD ["/tmp/docker_run.sh"]  
  
EXPOSE 80  
  
ENTRYPOINT ["/bin/bash"]  

