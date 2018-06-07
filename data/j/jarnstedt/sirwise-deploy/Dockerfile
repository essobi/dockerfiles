FROM webdevops/php-apache:ubuntu-16.04  
ENV PATH=/root/composer/vendor/bin:$PATH \  
COMPOSER_HOME=/root/composer \  
COMPOSER_ALLOW_SUPERUSER=1 \  
COMPOSER_HOME=/root/composer \  
APPLICATION_PATH="/project" \  
DEBIAN_FRONTEND=noninteractive  
  
RUN mkdir -p $APPLICATION_PATH/public \  
&& chown -R $APPLICATION_USER:$APPLICATION_GROUP $APPLICATION_PATH \  
&& curl -s
https://packagecloud.io/install/repositories/phalcon/stable/script.deb.sh |
bash \  
&& apt-add-repository ppa:ondrej/apache2 \  
&& LANG=C.UTF-8 apt-add-repository -y ppa:ondrej/php \  
&& echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d \  
&& apt-get update -y  
  
RUN apt-get -o Dpkg::Options::="--force-confnew" install -y -f --no-install-
recommends \  
php7.0-apcu \  
php-apcu-bc \  
php7.0-dev \  
php7.0-dba \  
php7.0-gmp \  
php-igbinary \  
php7.0-imagick \  
php7.0-imap \  
php-sodium \  
php-memcache \  
php7.0-mongodb \  
php7.0-msgpack \  
php-pear \  
php7.0-odbc \  
php-phalcon \  
php7.0-pspell \  
php7.0-recode \  
php-ssh2 \  
php7.0-tidy \  
php-yaml \  
lsb-release \  
libssh2-1-dev \  
libyaml-dev \  
libssl-dev  
  
RUN mkdir $COMPOSER_HOME \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& chmod +x /usr/local/bin/composer  
  
RUN TIMEZONE=`cat /etc/timezone`; sed -i "s|;date.timezone =.*|date.timezone =
${TIMEZONE}|" /etc/php/7.0/cli/php.ini \  
&& TIMEZONE=`cat /etc/timezone`; sed -i "s|;date.timezone =.*|date.timezone =
${TIMEZONE}|" /etc/php/7.0/fpm/php.ini \  
&& sed -i "s|memory_limit =.*|memory_limit = -1|" /etc/php/7.0/cli/php.ini \  
&& sed -i 's|short_open_tag =.*|short_open_tag = On|' /etc/php/7.0/cli/php.ini
\  
&& sed -i 's|error_reporting =.*|error_reporting = -1|'
/etc/php/7.0/cli/php.ini \  
&& sed -i 's|display_errors =.*|display_errors = On|' /etc/php/7.0/cli/php.ini
\  
&& sed -i 's|display_startup_errors =.*|display_startup_errors = On|'
/etc/php/7.0/cli/php.ini \  
&& sed -i -re 's|^(;?)(session.save_path) =.*|\2 = "/tmp"|g'
/etc/php/7.0/cli/php.ini \  
&& sed -i -re 's|^(;?)(phar.readonly) =.*|\2 = off|g' /etc/php/7.0/cli/php.ini
\  
&& echo "apc.enable_cli = 1" >> /etc/php/7.0/mods-available/apcu.ini  
  
# Install development tools  
RUN /usr/local/bin/apt-install graphviz php-xdebug \  
&& docker-image-cleanup  
  
# MongoDB tools  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927  
RUN echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2
multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list  
RUN apt-get update  
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y mongodb-org-tools
#mongodb-org  
RUN touch /lib/systemd/system/mongod.service  
  
# "codecept" and "sirwise" aliases  
RUN echo "alias codecept='./vendor/bin/codecept'" >> ~/.bashrc # Codeception
alias  
RUN echo "php /project/cli.php \$@" >> /bin/sirwise  
RUN chmod 755 /bin/sirwise  
  
RUN apt-get autoremove -y \  
&& apt-get autoclean -y \  
&& apt-get clean -y \  
&& rm -rf \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
/artifacts \  
/opt/docker/etc/php/fpm/pool.d/www.conf  
  
# Workaround for cron hard links error.  
RUN touch /etc/crontab /etc/cron.*/*  
RUN echo '' > /etc/crontab  
RUN echo '' > /etc/cron.d/php  
  
EXPOSE 80 443 9000  

