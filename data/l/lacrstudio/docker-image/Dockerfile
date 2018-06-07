FROM debian:latest  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get -y update && \  
apt-get -y install make gcc g++ curl git nodejs npm nano libssl-dev
libsqlite3-dev ruby ruby-dev mysql-client  
  
RUN echo "deb http://packages.dotdeb.org jessie all" >> /etc/apt/sources.list
&& \  
echo "deb-src http://packages.dotdeb.org jessie all" >> /etc/apt/sources.list  
  
RUN curl -O https://www.dotdeb.org/dotdeb.gpg && \  
apt-key add dotdeb.gpg  
  
RUN npm install -g grunt-cli  
  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
RUN npm install node-sass  
  
RUN npm rebuild node-sass  
  
RUN gem install capistrano capistrano-magento2 capistrano-locally mailcatcher  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get -y update && \  
apt-get install -y nginx && \  
apt-get install -y php5-fpm \  
php5-curl \  
php5-gd \  
php5-geoip \  
php5-intl \  
php5-json \  
php5-mcrypt \  
php5-memcached \  
php5-mysql \  
php5-xdebug \  
php5-xmlrpc \  
php5-xsl \  
php5-redis  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get install -y php7.0-fpm \  
php7.0-curl \  
php7.0-gd \  
php7.0-geoip \  
php7.0-intl \  
php7.0-json \  
php7.0-mbstring \  
php7.0-mcrypt \  
php7.0-memcached \  
php7.0-mysql \  
php7.0-opcache \  
php7.0-soap \  
php7.0-ssh2 \  
php7.0-xdebug \  
php7.0-xml \  
php7.0-xmlrpc \  
php7.0-xsl \  
php7.0-zip \  
php7.0-redis  
  
RUN apt-get install -y phpunit phing php-codesniffer phpmd  
  
RUN mkdir /etc/nginx/conf \  
&& php7.0 -r "copy('https://getcomposer.org/installer', 'composer-
setup.php');" \  
&& php7.0 composer-setup.php --install-dir=/usr/bin --filename=composer \  
&& php7.0 -r "unlink('composer-setup.php');"  
  
ADD files/nginx.conf /etc/nginx/  
ADD files/fastcgi_params /etc/nginx/conf/  
ADD files/servers.conf /etc/nginx/conf/  
ADD files/all.conf /etc/nginx/conf/  
ADD files/magento1.conf /etc/nginx/conf/  
ADD files/magento2.conf /etc/nginx/conf/  
ADD files/wordpress.conf /etc/nginx/conf/  
  
ADD files/php-fpm5.conf /etc/php5/fpm/php-fpm.conf  
ADD files/php-fpm7.conf /etc/php/7.0/fpm/php-fpm.conf  
  
ADD files/app_name-wildcard.pem /etc/nginx/  
ADD files/app_name-wildcard.key /etc/nginx/  
  
COPY startup.sh /usr/bin/startup.sh  
RUN chmod +x /usr/bin/startup.sh  
  
RUN sed -i \  
-e "s/^;sendmail_path.*/sendmail_path = \/usr\/local\/bin\/catchmail -f email@lacrbox.dev/" \  
/etc/php5/fpm/php.ini /etc/php5/cli/php.ini  
  
RUN sed -i \  
-e "s/^;sendmail_path.*/sendmail_path = \/usr\/local\/bin\/catchmail -f email@lacrbox.dev/" \  
/etc/php/7.0/fpm/php.ini /etc/php/7.0/cli/php.ini  
  
VOLUME ["/var/www/html"]  
WORKDIR /var/www/html  
  
EXPOSE 80 443 1025 1080  
# Entry point  
CMD ["/bin/bash", "/usr/bin/startup.sh"]  

