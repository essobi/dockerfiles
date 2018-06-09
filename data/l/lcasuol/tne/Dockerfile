#FROM khanhicetea/php7-fpm-docker  
FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
  
RUN apt-get clean && apt-get -y update && apt-get install -y locales curl
software-properties-common git \  
&& locale-gen en_US.UTF-8  
RUN LC_ALL=en_US.UTF-8 add-apt-repository ppa:ondrej/php  
  
RUN curl -sS http://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
  
RUN apt-get -y update  
RUN apt-get -y --force-yes upgrade  
RUN apt-get install -y --force-yes php7.1-bcmath php7.1-bz2 php7.1-cli
php7.1-common php7.1-curl \  
php7.1-cgi php7.1-dev php7.1-fpm php7.1-gd php7.1-gmp php7.1-imap php7.1-intl
\  
php7.1-json php7.1-ldap php7.1-mbstring php7.1-mcrypt php7.1-mysql \  
php7.1-odbc php7.1-opcache php7.1-pgsql php7.1-phpdbg php7.1-pspell \  
php7.1-readline php7.1-recode php7.1-soap php7.1-sqlite3 \  
php7.1-tidy php7.1-xml php7.1-xmlrpc php7.1-xsl php7.1-zip \  
php-tideways php-mongodb \  
vim nano supervisor nodejs duplicity \  
yarn apache2 apache2-utils libapache2-mod-php7.1 \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN a2enmod php7.1  
RUN a2enmod rewrite  
RUN a2enconf php7.1-fpm  
  
RUN curl -LO https://deployer.org/deployer.phar && mv deployer.phar
/usr/local/bin/dep && chmod +x /usr/local/bin/dep  
RUN curl -L https://getcomposer.org/installer > composer-setup.php && php
composer-setup.php && mv composer.phar /usr/local/bin/composer && rm composer-
setup.php  
  
COPY docker/apache/sites-available/* /etc/apache2/sites-available/  
COPY docker/apache/mysitename.crt /etc/apache2  
COPY docker/apache/mysitename.key /etc/apache2  
RUN chmod 600 /etc/apache2/mysite*  
COPY docker/cron/crontab /root/crontab  
RUN crontab /root/crontab  
  
#RUN useradd -d /home/app -m app  
#RUN adduser app www-data  
COPY . /var/www/html/transnat  
RUN chown -R www-data:www-data /var/www/html/transnat  
COPY docker/supervisor/conf.d/* /etc/supervisor/conf.d/  
RUN a2enmod ssl  
  
WORKDIR /var/www/html/transnat  
  
RUN composer install  
RUN yarn  
RUN yarn run production  
  
RUN chown -R www-data:www-data /var/www/html/transnat  
  
EXPOSE 8080  
#CMD 'php artisan serve --port=8080 --host=0.0.0.0'  
#USER root  
CMD "/usr/bin/supervisord"  

