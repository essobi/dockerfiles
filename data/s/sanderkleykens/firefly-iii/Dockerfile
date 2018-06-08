FROM ubuntu:16.04  
ARG FIREFLY_VERSION=4.0.2  
ARG FIREFLY_HOME=/opt/firefly  
ARG COMPOSER_VERSION=1.0.2  
ENV FIREFLY_CONFIG_APP_ENV=production  
ENV FIREFLY_CONFIG_APP_DEBUG=false  
ENV FIREFLY_CONFIG_APP_FORCE_SSL=false  
ENV FIREFLY_CONFIG_APP_FORCE_ROOT=  
ENV FIREFLY_CONFIG_APP_KEY=SomeRandomStringOf32CharsExactly  
ENV FIREFLY_CONFIG_APP_LOG_LEVEL=warning  
ENV FIREFLY_CONFIG_APP_URL=http://localhost  
ENV FIREFLY_CONFIG_DB_CONNECTION=mysql  
ENV FIREFLY_CONFIG_DB_HOST=127.0.0.1  
ENV FIREFLY_CONFIG_DB_PORT=3306  
ENV FIREFLY_CONFIG_DB_DATABASE=firefly  
ENV FIREFLY_CONFIG_DB_USERNAME=firefly  
ENV FIREFLY_CONFIG_DB_PASSWORD=  
ENV FIREFLY_CONFIG_COOKIE_PATH="/"  
ENV FIREFLY_CONFIG_COOKIE_DOMAIN=  
ENV FIREFLY_CONFIG_COOKIE_SECURE=false  
ENV FIREFLY_CONFIG_MAIL_DRIVER=smtp  
ENV FIREFLY_CONFIG_MAIL_HOST=  
ENV FIREFLY_CONFIG_MAIL_PORT=  
ENV FIREFLY_CONFIG_MAIL_FROM=  
ENV FIREFLY_CONFIG_MAIL_USERNAME=null  
ENV FIREFLY_CONFIG_MAIL_PASSWORD=null  
ENV FIREFLY_CONFIG_MAIL_ENCRYPTION=null  
ENV FIREFLY_CONFIG_SEND_REGISTRATION_MAIL=true  
ENV FIREFLY_CONFIG_MUST_CONFIRM_ACCOUNT=false  
ENV FIREFLY_CONFIG_SHOW_INCOMPLETE_TRANSLATIONS=false  
ENV FIREFLY_CONFIG_ANALYTICS_ID=  
ENV FIREFLY_CONFIG_SITE_OWNER=  
  
# Install php; v7 is default by ubuntu 16.04  
RUN apt-get update && \  
apt-get -y install \  
apt-utils \  
wget \  
git \  
zip \  
unzip \  
vim \  
nginx \  
mysql-client \  
postgresql-client \  
supervisor \  
php \  
php-cli \  
php-common \  
php-fpm \  
php-mysql \  
php-pgsql \  
php-curl \  
php-gd \  
php-imap \  
php-intl \  
php-json \  
php-mcrypt \  
php-readline \  
php-tidy \  
php-zip \  
php-bcmath \  
php-xml \  
php-mbstring \  
php-bz2 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install composer  
RUN wget https://getcomposer.org/download/${COMPOSER_VERSION}/composer.phar -O
/usr/local/bin/composer && \  
chmod +x /usr/local/bin/composer && \  
composer selfupdate  
  
# Install firefly  
RUN git clone \--branch "${FIREFLY_VERSION}" https://github.com/JC5/firefly-
iii.git --depth 1 "${FIREFLY_HOME}" && \  
cd "${FIREFLY_HOME}" && \  
composer install --no-scripts --no-dev  
RUN chown -R www-data "${FIREFLY_HOME}"  
  
# Add configuration  
ADD config/firefly/env "/var/firefly/env"  
ADD config/nginx/firefly /etc/nginx/sites-available/default  
ADD config/supervisor/supervisord.conf /etc/supervisor/supervisord.conf  
  
# Define docker entrypoint  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
ENTRYPOINT ["/bin/bash","--","/docker-entrypoint.sh"]  
  
# Bootstrap  
WORKDIR ${FIREFLY_HOME}  
EXPOSE 80  
CMD ["/usr/bin/supervisord", "-n"]  

