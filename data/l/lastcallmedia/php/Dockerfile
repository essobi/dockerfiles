  
FROM php:7.1-apache  
  
# common-php70  
ENV DEBIAN_FRONTEND noninteractive  
ENV APACHE_DOCROOT /var/www/html  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_REQUEST_WORKERS 150  
ENV PATH=/var/www/vendor/bin:$PATH  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
# for bz2  
bzip2 libbz2-dev \  
# for ftp  
libssl-dev \  
# for gd  
libfreetype6-dev libjpeg62-turbo-dev libpng12-dev \  
# for intl  
libicu-dev \  
# for dom  
libxml2-dev \  
# for ldap  
libldap2-dev \  
# for mcrypt  
libmcrypt-dev \  
# for mysql  
mysql-client \  
# for git  
git \  
# for ssh client only  
openssh-client \  
# For image optimization  
jpegoptim \  
optipng \  
pngquant \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu \  
&& docker-php-ext-install -j$(nproc) \  
bcmath \  
bz2 \  
calendar \  
exif \  
ftp \  
gd \  
gettext \  
intl \  
ldap \  
mcrypt \  
mysqli \  
opcache \  
pcntl \  
pdo_mysql \  
shmop \  
soap \  
sockets \  
sysvmsg \  
sysvsem \  
sysvshm \  
zip \  
&& pecl install redis apcu \  
&& docker-php-ext-enable redis apcu \  
# Set a reasonable max upload size  
&& printf "upload_max_filesize = 128M\npost_max_size = 128M" >
$PHP_INI_DIR/conf.d/00-max_filesize.ini  
  
# Configure Apache:  
RUN a2enmod rewrite headers expires \  
&& sed -i "/User www-data/c\User \$\\{APACHE_RUN_USER\\}"
/etc/apache2/apache2.conf \  
&& sed -i "/Group www-data/c\Group \$\\{APACHE_RUN_GROUP\\}"
/etc/apache2/apache2.conf \  
&& sed -i "/DocumentRoot \/var\/www\/html/c\\\\\tDocumentRoot
\$\\{APACHE_DOCROOT\\}" /etc/apache2/sites-enabled/000-default.conf \  
# Preemptively add a user 1000, for use with $APACHE_RUN_USER on osx  
&& adduser --uid 1000 \--gecos 'My OSX User' \--disabled-password osxuser  
  
# Install CLI tools:  
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/bin/composer \  
&& mkdir /usr/share/composer \  
&& cd /usr/share/composer \  
&& composer init --no-interaction && composer config bin-dir /usr/local/bin \  
&& composer require drush/drush --prefer-dist \  
&& rm -r /root/.composer/cache \  
&& curl -L
https://github.com/jwilder/dockerize/releases/download/v0.6.0/dockerize-linux-
amd64-v0.6.0.tar.gz | tar -C /usr/local/bin -xzv \  
&& chmod +x /usr/local/bin/dockerize \  
&& ssh-keyscan github.com >> /etc/ssh/ssh_known_hosts  
  
ADD mpm_prefork.conf /etc/apache2/mods-enabled/mpm_prefork.conf  
ADD scripts/* /usr/local/bin/  
CMD ["apache2-foreground-enhanced"]  
# /common-php70  
# Install development tools.  
# We install nvm, but also add node to $PATH directly  
# so we can use it through /bin/sh.  
ENV NVM_DIR /usr/local/nvm  
ENV NODE_VERSION v6.11.0  
ENV NODE_PATH $NVM_DIR/versions/node/$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/versions/node/$NODE_VERSION/bin:$PATH  
ENV PHANTOMJS_VERSION 2.1.1  
  
RUN pecl install xdebug \  
&& docker-php-ext-enable xdebug \  
&& echo "xdebug.default_enable=0\nxdebug.coverage_enable=0" >
$PHP_INI_DIR/conf.d/xdebug.ini \  
# Nodejs, installed globally via nvm for all bash users.  
&& curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.33.6/install.sh |
PROFILE=/etc/bash.bashrc bash \  
&& . $NVM_DIR/nvm.sh \  
&& nvm install $NODE_VERSION \  
&& npm install -g yarn \  
# Install Gulp  
&& npm install -g gulp \  
# Install PhantomJS  
&& apt-get update \  
# Install fonts and libtdl (for mounted docker binary usage)  
&& apt-get install -y libfontconfig libltdl7 \  
&& curl -sL
"https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${PHANTOMJS_VERSION}-linux-x86_64.tar.bz2"
| tar jx \  
&& mv phantomjs-${PHANTOMJS_VERSION}-linux-x86_64 /usr/local/bin/phantomjs \  
# Install Blackfire Probe  
&& version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \  
&& curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/$version \  
&& tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
&& mv /tmp/blackfire-*.so $(php -r "echo
ini_get('extension_dir');")/blackfire.so \  
&& printf
"extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707\n" >
$PHP_INI_DIR/conf.d/blackfire.ini \  
# Install blackfire CLI  
&& mkdir -p /tmp/blackfire \  
&& curl -A "Docker" -L
https://blackfire.io/api/v1/releases/client/linux_static/amd64 | tar zxp -C
/tmp/blackfire \  
&& mv /tmp/blackfire/blackfire /usr/bin/blackfire \  
&& rm -Rf /tmp/blackfire \  
# Install Terminus  
&& mkdir /usr/share/terminus \  
&& composer --working-dir=/usr/share/terminus init -n && composer --working-
dir=/usr/share/terminus config bin-dir /usr/local/bin \  
&& composer --working-dir=/usr/share/terminus require pantheon-
systems/terminus \--prefer-dist \  
&& rm -r /root/.composer/cache \  
# Clean up the leftovers  
&& npm cache clean --force \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY test-dev.sh /test.sh  

