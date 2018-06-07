FROM ubuntu:xenial  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get upgrade -y  
  
ENV TZ Asia/Shanghai  
ENV TERM xterm  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \  
php7.0 \  
php7.0-bz2 \  
php7.0-cgi \  
php7.0-cli \  
php7.0-common \  
php7.0-curl \  
php7.0-enchant \  
php7.0-fpm \  
php7.0-gd \  
php7.0-gmp \  
php7.0-imap \  
php7.0-intl \  
php7.0-json \  
php7.0-ldap \  
php7.0-mysql \  
php7.0-odbc \  
php7.0-opcache \  
php7.0-pgsql \  
php7.0-phpdbg \  
php7.0-sqlite3 \  
php7.0-tidy \  
php7.0-xmlrpc \  
php7.0-xsl \  
php7.0-zip \  
php7.0-mbstring \  
php-redis \  
php-xdebug  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install supervisor -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get install apache2 libapache2-mod-
php7.0 -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get install curl vim-tiny -y  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& composer config -g repo.packagist composer
https://packagist.phpcomposer.com  
  
COPY index.php /var/www/html/  
COPY sources.list /etc/apt/  
COPY php.ini /etc/php/7.0/apache2/  
COPY apache2/apache2.conf /etc/apache2/  
COPY apache2/dir.conf /etc/apache2/mods-enabled/  
COPY apache2/000-default.conf /etc/apache2/sites-enabled/  
COPY run.sh /usr/local/bin/  
  
COPY supervisord-apache2.conf /etc/supervisor/conf.d/  
  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime  
RUN echo $TZ > /etc/timezone  
RUN dpkg-reconfigure -f noninteractive tzdata  
RUN sed -i "s%\;date\\.timezone\ \=%date\\.timezone\ \=\ ${TZ}%"
/etc/php/7.0/apache2/php.ini  
  
RUN a2enmod rewrite  
RUN sed -i 's/AllowOverride\ None/AllowOverride\ All/g'
/etc/apache2/apache2.conf  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf  
  
RUN chmod 755 /usr/local/bin/*.sh  
  
VOLUME /var/www/html  
  
EXPOSE 80  
CMD ["/usr/local/bin/run.sh"]  

