FROM php:latest  
MAINTAINER Maarten Bode <maarten@orangetalent.nl>  
  
RUN export DEBIAN_FRONTEND=noninteractive  
  
# Update installation and install git, nodejs, npm and yarn + dependencies  
RUN apt-get update  
RUN apt-get install -y apt-transport-https ca-certificates wget gnupg  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
E1DD270288B4E6030699E45FA1715D88E1DF1F24  
RUN echo "deb http://ppa.launchpad.net/git-core/ppa/ubuntu trusty main" >>
/etc/apt/sources.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
9FD3B784BC1C6FC31A8A0A1C1655A0AB68576280  
RUN echo "deb https://deb.nodesource.com/node_8.x trusty main" >>
/etc/apt/sources.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 86E50310  
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update  
RUN apt-get install -y git-core openssh-client curl libapparmor1 nodejs git-
ftp libbz2-dev libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev libpng-dev
libgmp-dev libgmp3-dev libc-client2007e-dev zlib1g-dev libicu-dev g++
libpspell-dev libxml2-dev libsqlite3-dev libxslt-dev yarn locales locales-all  
RUN rm -rf /var/lib/apt/lists/*  
  
# Install php extensions using built-in tools  
RUN ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h  
RUN docker-php-source extract \  
&& docker-php-ext-install -j$(nproc) bcmath bz2 calendar dba exif ftp gd
gettext gmp intl hash mysqli pcntl pdo_mysql pspell shmop soap sockets
pdo_sqlite sysvmsg sysvsem sysvshm wddx xmlrpc xsl zip \  
&& docker-php-source delete \  
;  
  
# Install xdebug php extension  
# RUN pecl install xdebug \  
# && echo "zend_extension=xdebug.so" > /usr/local/etc/php/conf.d/xdebug.ini \  
# ;  
# Install composer  
RUN curl -sL https://getcomposer.org/composer.phar -o /usr/local/bin/composer
&& chmod +x /usr/local/bin/composer  
  
# Install phploy  
RUN curl -sL
https://github.com/banago/PHPloy/raw/d22d532c118049abda5a86607ed8f99095d349be/dist/phploy.phar
-o /usr/local/bin/phploy && chmod +x /usr/local/bin/phploy  
  
# Install Deployer  
RUN curl -LO https://deployer.org/deployer.phar && mv deployer.phar
/usr/local/bin/dep && chmod +x /usr/local/bin/dep  
  
# Install PHPUnit  
RUN curl -sL https://phar.phpunit.de/phpunit.phar -o /usr/local/bin/phpunit &&
chmod +x /usr/local/bin/phpunit  
  
# Add Deployer recipes  
RUN composer require deployer/recipes --dev  
  
ENV COMPOSER_CACHE_DIR /cache/composer  
ENV YARN_CACHE_FOLDER /cache/yarn  
ENV NPM_CONFIG_CACHE /cache/npm  
ENV GEM_SPEC_CACHE /cache/gem  
ENV PIP_DOWNLOAD_CACHE /cache/pip  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
CMD [ "bash" ]  

