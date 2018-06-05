FROM php:7.2-apache  
# Install PHP extensions and utilities  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \--no-install-recommends
\  
libicu-dev \  
libmcrypt-dev \  
zlib1g-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng-dev \  
nano \  
&& docker-php-ext-configure pdo_mysql \--with-pdo-mysql=mysqlnd \  
&& docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ \--with-
jpeg-dir=/usr/include/ \  
&& docker-php-ext-install \  
intl \  
mbstring \  
pcntl \  
pdo_mysql \  
zip \  
opcache \  
&& docker-php-ext-install -j$(nproc) gd \  
&& pecl install mcrypt-1.0.1 \  
&& pecl install xdebug-2.6.0 \  
&& docker-php-ext-enable mcrypt xdebug \  
&& apt-get remove -y \--purge \  
libicu-dev \  
libmcrypt-dev \  
zlib1g-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng-dev \  
&& apt-get clean && rm -rf /tmp/* /var/tmp/* && rm -rf /var/lib/apt/lists/*  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- \--install-
dir=/usr/bin \--filename=composer  
# OpenShift Origin runs containers using an arbitrarily assigned user ID  
# (random UID) and root group. The user ID of the container is generated  
# dynamically, it will not have an associated entry in /etc/passwd.  
# https://docs.openshift.org/latest/creating_images/guidelines.html  
# Thus, in order to drop the root user, we have to:  
# 1. Run apache2 on a custom port (8080), a non-root user does not have access
to port 80.  
# 2. Make some directories world writeable.  
# https://askubuntu.com/a/338239  
# https://github.com/openshift/origin/issues/6629  
RUN sed -i "s/Listen 80/Listen 8080/g" /etc/apache2/ports.conf \  
&& sed -i "s/<VirtualHost \\*:80>/<VirtualHost \\*:8080>/g"
/etc/apache2/sites-enabled/000-default.conf  
RUN mkdir -p /var/run/apache2 && chmod 777 -R /var/run/apache2 \  
&& mkdir -p /var/log/apache2 && chmod 777 -R /var/log/apache2 \  
&& mkdir -p /var/lock/apache2 && chmod 777 -R /var/lock/apache2 \  
&& mkdir -p /etc/apache2/sites-enabled && chmod 777 -R /etc/apache2/sites-
enabled \  
&& mkdir -p /var/www/html && chmod 777 -R /var/www/html  
# Compare also with:  
# https://github.com/sclorg/s2i-php-container/  
# https://github.com/openshift-qe/ssh-git-docker/blob/master/ssh-git-
openshift/Dockerfile  
  
COPY deploy/config/docker/docker-php-entrypoint /usr/local/bin/  
RUN chmod 755 /usr/local/bin/docker-php-entrypoint \  
&& chmod 664 /etc/passwd \  
&& mkdir -p /home/openshift \  
&& chmod 777 -R /home/openshift  
# Put apache config for Laravel  
COPY deploy/config/apache/arecocla.conf /etc/apache2/sites-
available/arecocla.conf  
RUN a2dissite 000-default.conf && a2ensite arecocla.conf && a2enmod rewrite  
  
# Put application code  
RUN mkdir -p -m 777 /var/www/html/bootstrap/cache \  
/var/www/html/public/uploads/app/categories/custom \  
/var/www/html/public/uploads/app/ico \  
/var/www/html/public/uploads/app/logo \  
/var/www/html/public/uploads/app/page \  
/var/www/html/public/uploads/files \  
/var/www/html/storage/app/public \  
/var/www/html/storage/app/purifier \  
/var/www/html/storage/dotenv-editor \  
/var/www/html/storage/framework/cache \  
/var/www/html/storage/framework/sessions \  
/var/www/html/storage/framework/testing \  
/var/www/html/storage/framework/views \  
/var/www/html/storage/logs  
  
COPY deploy/config/apache/.htaccess-root /var/www/html/.htaccess  
COPY deploy/config/apache/.htaccess-public /var/www/html/public/.htaccess  
COPY deploy/config/arecocla/.env.example /var/www/html/.env.example  
#TODO: EXLUDE DOCS & OTHERS and ADD .htaccess, .env, etc  
COPY src /var/www/html  
#VOLUME /var/www/html  
WORKDIR /var/www/html  
  
EXPOSE 8080  
  
# Set labels used in OpenShift to describe the builder images  
LABEL maintainer="Santiago Iagrossi <santiago.iagrossi@gmail.com>" \  
io.k8s.description="Arecoclasificados Webapp Container" \  
io.k8s.display-name="arecocla" \  
io.openshift.expose-services="8080:http" \  
io.openshift.tags="builder,html,apache,php7,laravel" \  
io.openshift.min-memory="256Mi" \  
io.openshift.min-cpu="1" \  
io.openshift.non-scalable="false"  

