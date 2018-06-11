FROM versantus/webserver-dev:php7-xdebug  
  
RUN ln -sf /usr/bin/php7.0 /usr/bin/php && \  
apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
openssh-client \  
rsync \  
wget \  
gzip \  
tar \  
patch \  
perl \  
php-pear \  
libpcre3-dev \  
imagemagick \  
php-imagick \  
php7.0-bcmath \  
php-curl\  
emacs-nox\  
&& rm -r /var/lib/apt/lists/*  
  
WORKDIR /var/www/html  
  
COPY apache.conf /etc/apache2/sites-available/000-default.conf  
COPY php.ini /etc/php/7.0/apache2/php.ini  
RUN ln -sf /dev/stdout /var/log/apache2/other_vhosts_access.log \  
&& ln -sf /dev/stderr /var/log/apache2/default_error_log  
  
RUN set -ex \  
&& buildDeps=' \  
libpng12-dev \  
libpq-dev \  
' \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates $buildDeps && rm -rf /var/lib/apt/lists/* \  
&& apt-mark manual \  
libpq5 \  
&& apt-get purge -y --auto-remove $buildDeps  
  
WORKDIR /var/www/html  
  
RUN php7.0 -r "readfile('https://github.com/drush-
ops/drush/releases/download/8.1.3/drush.phar');" > drush && chmod +x drush &&
mv drush /usr/bin/ \  
&& php7.0 -r "readfile('https://raw.githubusercontent.com/wp-cli/builds/gh-
pages/phar/wp-cli.phar');" > wp && chmod +x wp && mv wp /usr/bin/ \  
&& mkdir /var/www/tmp \  
&& chmod 755 -R /var/www/tmp \  
&& chown www-data:www-data /var/www/tmp  
  

