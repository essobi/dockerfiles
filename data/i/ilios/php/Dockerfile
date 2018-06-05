FROM ilios/source:v3.41.0  
  
MAINTAINER Ilios Project Team <support@iliosproject.org>  
  
RUN apk add --update \  
curl \  
tar \  
php7 \  
php7-fpm \  
php7-apcu \  
php7-dom \  
php7-json \  
php7-ldap \  
php7-opcache \  
php7-openssl \  
php7-pdo \  
php7-pdo_mysql \  
php7-xml \  
php7-xmlreader \  
php7-curl \  
php7-zlib \  
php7-phar \  
php7-mbstring \  
php7-session \  
php7-ctype  
  
RUN ln -s /usr/bin/php7 /usr/bin/php  
RUN ln -s /usr/sbin/php-fpm7 /usr/sbin/php-fpm  
RUN rm -rf /var/cache/apk/* && rm -rf /tmp/*  
  
ADD ilios.ini /etc/php7/fpm/conf.d/  
ADD ilios.ini /etc/php7/cli/conf.d/  
ADD php-fpm.conf /etc/php7/  
  
VOLUME /data  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
ENV COMPOSER_HOME=/tmp \  
SYMFONY_ENV=prod \  
ILIOS_API_ENVIRONMENT=prod \  
ILIOS_API_DEBUG=false \  
ILIOS_DATABASE_DRIVER=pdo_mysql \  
ILIOS_DATABASE_HOST=db \  
ILIOS_DATABASE_PORT=~ \  
ILIOS_DATABASE_NAME=ilios \  
ILIOS_DATABASE_USER=ilios \  
ILIOS_DATABASE_PASSWORD=ilios \  
ILIOS_DATABASE_MYSQL_VERSION=5.7 \  
ILIOS_MAILER_TRANSPORT=smtp \  
ILIOS_MAILER_HOST=127.0.0.1 \  
ILIOS_MAILER_USER=~ \  
ILIOS_MAILER_PASSWORD=~ \  
ILIOS_LOCALE=en \  
ILIOS_SECRET=ThisTokenIsNotSoSecretChangeIt \  
ILIOS_AUTHENTICATION_TYPE=form \  
ILIOS_LEGACY_PASSWORD_SALT=null \  
ILIOS_FILE_SYSTEM_STORAGE_PATH=/data \  
ILIOS_INSTITUTION_DOMAIN=example.com \  
ILIOS_SUPPORTING_LINK=null \  
ILIOS_LDAP_AUTHENTICATION_HOST=null \  
ILIOS_LDAP_AUTHENTICATION_PORT=null \  
ILIOS_LDAP_AUTHENTICATION_BIND_TEMPLATE=null \  
ILIOS_LDAP_DIRECTORY_URL=null \  
ILIOS_LDAP_DIRECTORY_USER=null \  
ILIOS_LDAP_DIRECTORY_PASSWORD=null \  
ILIOS_LDAP_DIRECTORY_SEARCH_BASE=null \  
ILIOS_LDAP_DIRECTORY_CAMPUS_ID_PROPERTY=null \  
ILIOS_LDAP_DIRECTORY_USERNAME_PROPERTY=null \  
ILIOS_SHIBBOLETH_AUTHENTICATION_LOGIN_PATH=null \  
ILIOS_SHIBBOLETH_AUTHENTICATION_LOGOUT_PATH=null \  
ILIOS_SHIBBOLETH_AUTHENTICATION_USER_ID_ATTRIBUTE=null \  
ILIOS_TIMEZONE='America/Los_Angeles' \  
ILIOS_REQUIRE_SECURE_CONNECTION=false \  
ILIOS_KEEP_FRONTEND_UPDATED=true \  
ILIOS_FRONTEND_RELEASE_VERSION=null \  
ILIOS_CAS_AUTHENTICATION_SERVER=null \  
ILIOS_CAS_AUTHENTICATION_VERSION=3 \  
ILIOS_CAS_AUTHENTICATION_VERIFY_SSL=true \  
ILIOS_CAS_AUTHENTICATION_CERTIFICATE_PATH=null \  
ILIOS_ENABLE_TRACKING=false \  
ILIOS_TRACKING_CODE=UA-XXXXXXXX-1  
  
USER nobody  
RUN /usr/local/bin/composer install \  
\--working-dir /var/www/ilios \  
\--prefer-dist \  
\--no-dev \  
\--no-progress \  
\--no-interaction \  
\--no-suggest \  
\--classmap-authoritative  
  
RUN /var/www/ilios/bin/console ilios:maintenance:update-frontend  
  
USER root  
CMD ["php-fpm", "-F"]  
  
EXPOSE 9000  

