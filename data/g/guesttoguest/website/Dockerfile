FROM php:5.6-fpm  
  
MAINTAINER GuestToGuest software team <dev@guesttoguest.com>  
  
# nginx and php-fpm user MUST be the same  
RUN usermod -u 1000 www-data  
  
# set php date.timezone  
RUN touch /usr/local/etc/php/conf.d/php.ini  
RUN echo "date.timezone = UTC" >> /usr/local/etc/php/conf.d/php.ini  
  
RUN apt-get update && apt-get install -y apt-utils apt-transport-https uuid-
dev  
  
# composer install  
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer  
  
# add Yarn source package  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
# install php extensions dependencies  
#RUN echo 'Dir::Ignore-Files-Silently:: "(.save|.distupgrade)$";' >
/etc/apt/apt.conf.d/99ignoresave  
RUN apt-get update && apt-get install -my vim nano mysql-client mlocate wget
libcurl4-gnutls-dev gettext \  
zlib1g-dev libgdbm-dev libpng-dev libmcrypt-dev libmysqlclient15-dev libicu-
dev g++ zip build-essential \  
ruby-full python-setuptools python-dev git  
  
# install Prestissimo for Composer  
RUN export COMPOSER_HOME=/root && /usr/local/bin/composer global require
"hirak/prestissimo:^0.3"  
  
# python  
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python  
RUN pip install boto3==1.3.0  
  
# nodejs & yarn  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs yarn  
  
# gems  
RUN gem install --no-rdoc --no-ri sass -v 3.4.18  
RUN gem install --no-rdoc --no-ri compass -v 1.0.3  
RUN gem install --no-rdoc --no-ri bootstrap-sass -v 3.3.6  
RUN gem install --no-rdoc --no-ri font-awesome-sass -v 4.5.0  
  
# install php extensions  
RUN docker-php-ext-install curl  
RUN docker-php-ext-install gd  
RUN docker-php-ext-install mysql  
RUN docker-php-ext-install pdo_mysql  
RUN docker-php-ext-install json  
RUN docker-php-ext-install mcrypt  
RUN docker-php-ext-install intl  
RUN docker-php-ext-install opcache  
RUN pecl install APCu-4.0.10 && docker-php-ext-enable apcu  
RUN echo "" | pecl install uuid  
RUN docker-php-ext-enable uuid  
  
# configure extensions#  
RUN { \  
echo 'zend_extension=/usr/local/lib/php/extensions/no-debug-non-
zts-20131226/opcache.so'; \  
echo 'opcache.memory_consumption=256'; \  
echo 'opcache.interned_strings_buffer=16'; \  
echo 'opcache.max_accelerated_files=20000'; \  
echo 'opcache.revalidate_freq=2'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/docker-php-ext-opcache.ini  
  
# install xdebug for dev env  
#RUN pecl install xdebug && docker-php-ext-enable xdebug  
#RUN { \  
# echo 'zend_extension=/usr/local/lib/php/extensions/no-debug-non-
zts-20131226/xdebug.so'; \  
# echo 'xdebug.profiler_enable=0'; \  
# echo 'xdebug.profiler_enable_trigger=0'; \  
# echo 'xdebug.profiler_output_dir=/tmp/xdebug'; \  
# echo 'xdebug.max_nesting_level= 500'; \  
# } > /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  

