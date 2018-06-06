FROM ubuntu:17.10  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y apt-utils \  
curl \  
wget \  
unzip \  
git \  
mysql-client \  
sudo \  
vim \  
bzip2 \  
htop \  
software-properties-common \  
python-software-properties \  
build-essential \  
libssl-dev \  
php7.1-common \  
php-apcu \  
php7.1-curl \  
php7.1-dev \  
php7.1-mcrypt \  
php7.1-mysql \  
php7.1-curl \  
php7.1-soap \  
php7.1-intl \  
php7.1-gd \  
php7.1-mbstring \  
php7.1-zip \  
php7.1-xml \  
php-xdebug \  
php-pear \  
php-memcache \  
libapache2-mod-php7.1 \  
libsqlite3-dev \  
ruby \  
ruby-dev \  
command-not-found  
  
# install the utils extensions we need  
## COMPOSER ##  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php composer-setup.php \  
&& php -r "unlink('composer-setup.php');" \  
&& chmod +x composer.phar \  
&& mv composer.phar /usr/local/bin/composer  
## DRUSH ##  
RUN wget http://files.drush.org/drush.phar \  
&& chmod +x drush.phar \  
&& mv drush.phar /usr/local/bin/drush  
## WP CLI ##  
RUN wget https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar \  
&& chmod +x wp-cli.phar \  
&& mv wp-cli.phar /usr/local/bin/wp  
## NODE with NVM, GRUNT, BOWER ##  
# Replace shell with bash so we can source files  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
ENV NVM_DIR /usr/local/nvm  
RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh |
PROFILE=/etc/bash.bashrc /bin/bash \  
&& source $NVM_DIR/nvm.sh \  
&& nvm install 8 \  
&& nvm install 6 \  
&& nvm install 4 \  
&& nvm alias default 8 \  
&& nvm use default \  
&& npm install npm -g \  
&& npm install -g grunt-cli bower http-server  
## YARN ##  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg \  
&& apt-key add -echo "deb https://dl.yarnpkg.com/debian/ stable main" \  
&& tee /etc/apt/sources.list.d/yarn.list \  
&& apt-get update && apt-get install -y yarn  
  
## SOME HACK on PHP ##  
RUN echo 'xdebug.remote_enable = 1' >>
/etc/php/7.1/apache2/conf.d/20-xdebug.ini \  
&& echo 'xdebug.remote_connect_back = 1' >>
/etc/php/7.1/apache2/conf.d/20-xdebug.ini \  
&& echo 'xdebug.remote_port = 9009' >>
/etc/php/7.1/apache2/conf.d/20-xdebug.ini \  
&& echo 'xdebug.idekey = "PHPSTORM"' >>
/etc/php/7.1/apache2/conf.d/20-xdebug.ini \  
&& echo "xdebug.default_enable = 0" >>
/etc/php/7.1/apache2/conf.d/20-xdebug.ini \  
&& echo "xdebug.remote_autostart = 0" >>
/etc/php/7.1/apache2/conf.d/20-xdebug.ini \  
&& echo "xdebug.profiler_enable = 1" >>
/etc/php/7.1/apache2/conf.d/20-xdebug.ini \  
&& echo "xdebug.remote_host = 172.17.0.1" >>
/etc/php/7.1/apache2/conf.d/20-xdebug.ini \  
&& echo 'date.timezone = "Europe/Rome"' >>
/etc/php/7.1/apache2/conf.d/90-override.ini \  
&& echo 'memory_limit = 512M' >> /etc/php/7.1/apache2/conf.d/90-override.ini \  
&& echo 'upload_max_filesize = 80M' >>
/etc/php/7.1/apache2/conf.d/90-override.ini \  
&& echo 'sendmail_path = /usr/bin/env catchmail -f no-reply@dev.env' >>
/etc/php/7.1/apache2/conf.d/90-override.ini  
  
RUN rm /etc/php/7.1/apache2/conf.d/10-opcache.ini  
RUN a2enmod rewrite && a2enmod proxy && a2enmod proxy_http  
  
RUN gem install mailcatcher && mailcatcher  
  
ADD conf/10-sameuser-nopass /etc/sudoers.d/  
ADD conf/user.sh /  
RUN /user.sh  
COPY conf/httpd-foreground /usr/local/bin/  
  
EXPOSE 80  
EXPOSE 1025  
EXPOSE 1080  
  
WORKDIR /var/www/html  
  
CMD ["httpd-foreground"]  

