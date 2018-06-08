FROM ubuntu:16.04  
MAINTAINER "Thaweesak Chusri" <t.chusri@gmail.com>  
  
# Upgrade  
RUN apt-get update -y  
RUN apt-get upgrade -y  
  
# Install Nginx  
RUN apt-get install -y nginx  
RUN ip addr show eth0 | grep inet | awk '{ print $2; }' | sed 's/\/.*$//'  
  
# Apply Nginx configuration  
# ADD config/nginx.conf /opt/etc/nginx.conf  
RUN rm /etc/nginx/sites-available/default  
RUN rm /etc/nginx/sites-enabled/default  
ADD config/default /etc/nginx/sites-available/default  
RUN ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default  
  
RUN mkdir -p /data  
VOLUME ["/data"]  
  
RUN apt-get update -y && apt-get install -y software-properties-common python-
software-properties  
RUN LC_ALL=C.UTF-8 add-apt-repository -y -u ppa:ondrej/php  
RUN apt-get update -y  
  
# Install PHP-FPM and popular/laravel required extensions  
RUN apt-get install -y \  
zip \  
unzip \  
curl \  
git \  
php7.1-fpm \  
php7.1-mcrypt \  
php7.1-mysql \  
php7.1-mbstring \  
php7.1-curl \  
php7.1-gd \  
php7.1-intl \  
php7.1-imagick \  
php7.1-imap \  
php7.1-memcache \  
php7.1-pspell \  
php7.1-recode \  
php7.1-sqlite3 \  
php7.1-tidy \  
php7.1-xmlrpc \  
php7.1-xsl \  
php7.1-mbstring \  
php7.1-gettext \  
php7.1-mongodb \  
php7.1-ldap \  
vim \  
cron  
  
# Configure PHP-FPM  
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/"
/etc/php/7.1/fpm/php.ini  
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/"
/etc/php/7.1/fpm/php.ini  
# RUN echo "xdebug.max_nesting_level=500" > /etc/php5/mods-
available/xdebug.ini  
# sed -i "s/display_errors = Off/display_errors = stderr/"
/etc/php/7.1/fpm/php.ini && \  
# sed -i "s/upload_max_filesize = 2M/upload_max_filesize = 30M/"
/etc/php/7.1/fpm/php.ini && \  
# sed -i "s/;opcache.enable=0/opcache.enable=0/" /etc/php/7.1/fpm/php.ini && \  
# sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-
fpm.conf && \  
# sed -i '/^listen = /clisten = 9000' /etc/php5/fpm/pool.d/www.conf && \  
# sed -i '/^listen.allowed_clients/c;listen.allowed_clients ='
/etc/php5/fpm/pool.d/www.conf && \  
# sed -i '/^;catch_workers_output/ccatch_workers_output = yes'
/etc/php5/fpm/pool.d/www.conf && \  
# sed -i '/^;env\\[TEMP\\] = .*/aenv[DB_PORT_3306_TCP_ADDR] =
$DB_PORT_3306_TCP_ADDR' /etc/php5/fpm/pool.d/www.conf  
RUN phpenmod mcrypt  
RUN phpenmod mbstring  
  
# Composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
RUN composer self-update  
  
# Data Volume  
# RUN mkdir -p /data/logs/ /data/www/  
RUN mkdir -p /data/  
RUN ls /data  
VOLUME ["/data"]  
  
COPY config/nginx.conf /etc/nginx/nginx.conf  
  
RUN apt-get -o Dpkg::Options::="--force-overwrite" install -y nginx-extras
openjdk-8-jdk  
RUN apt-get install -y wget  
RUN wget
https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.2.2.tar.gz  
RUN mkdir -p /run  
RUN tar xvfz elasticsearch-6.2.2.tar.gz  
RUN mv elasticsearch-6.2.2 /run/elasticsearch  
ENV TZ=Asia/Bangkok  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
RUN adduser --disabled-password --gecos "" elastic  
  
RUN chown -R elastic:elastic /run/elasticsearch  
  
RUN mkdir -p /run/php  
# PORTS  
EXPOSE 80  
EXPOSE 443  
EXPOSE 9000  
WORKDIR /data  
  
# Nginx startup script  
ADD config/nginx-start.sh /opt/bin/nginx-start.sh  
RUN chmod u=rwx /opt/bin/nginx-start.sh  
  
ENTRYPOINT ["/opt/bin/nginx-start.sh"]  

