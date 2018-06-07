FROM php:7.1-cli  
  
LABEL maintainer="Mriyam Tamuli <mbtamuli@gmail.com>"  
  
RUN echo "memory_limit=-1" > "$PHP_INI_DIR/conf.d/memory-limit.ini" \  
&& echo "date.timezone=Asia/Kolkata" > "$PHP_INI_DIR/conf.d/date_timezone.ini"  
  
VOLUME /root/composer  
ENV HOME /root  
ENV PATH "/composer/vendor/bin:~/.local/bin:$PATH"  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_HOME /composer  
ENV COMPOSER_VERSION 1.5.6  
ENV NVM_DIR "$HOME/.nvm"  
ENV NODE_VERSION lts  
  
# Packages  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
apt-transport-https \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libbz2-dev \  
libxslt-dev \  
curl \  
git \  
subversion \  
zip unzip \  
wget \  
mariadb-server \  
libmemcached-dev libmemcached11 \  
python-pip \  
python-dev \  
libyaml-dev \  
&& rm -r /var/lib/apt/lists/*  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Installing awscli  
RUN pip install --quiet awscli --upgrade --user  
  
# PHP Extensions  
RUN docker-php-ext-install bcmath mcrypt zip bz2 mbstring pcntl xsl \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install mysqli  
  
RUN cd /tmp \  
&& git clone https://github.com/bnap00/pecl-memcache.git memcache \  
&& cd memcache \  
&& /usr/local/bin/phpize \  
&& ./configure --with-php-config=/usr/local/bin/php-config \  
&& make \  
&& make install \  
&& echo "extension=/usr/local/lib/php/extensions/no-debug-non-
zts-20160303/memcache.so" > /usr/local/etc/php/conf.d/ext-memcache.ini \  
&& rm -rf /tmp/memcache  
  
# Start MYSQL Service and set root password as root  
RUN service mysql start && mysql -e "create database wp" && mysqladmin -u root
password root  
  
# Setup the Composer installer  
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }"  
  
# Install Composer  
RUN mkdir -p /composer  
RUN php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer --version=${COMPOSER_VERSION} && rm -rf /tmp/composer-
setup.php  
COPY composer.* /composer/  
RUN cd /composer && composer install  
  
# Download and load nvm in environment  
RUN wget -qO-
https://raw.githubusercontent.com/creationix/nvm/v0.33.6/install.sh | bash  
# install node and npm  
RUN bash -c "[ -s $NVM_DIR/nvm.sh ] && \\. $NVM_DIR/nvm.sh \  
&& nvm install --lts \  
&& nvm use default"  
  
# install yarn  
RUN bash -c "[ -s $NVM_DIR/nvm.sh ] && \\. $NVM_DIR/nvm.sh \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& echo \"deb https://dl.yarnpkg.com/debian/ stable main\" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update > /dev/null && apt-get install yarn -qqy \  
&& yarn config set cache-folder ~/.yarn_cache"  

