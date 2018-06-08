FROM ubuntu:16.04  
MAINTAINER Aleksandr Belous  
  
RUN apt-get update -y  
RUN apt-get install -y \  
vim \  
zip \  
curl \  
wget \  
apache2 \  
php7.0 \  
php7.0-cli \  
libapache2-mod-php7.0 \  
php7.0-intl \  
php7.0-gd \  
php7.0-curl \  
php7.0-mysql \  
php-pear \  
php7.0-dev \  
php-xdebug \  
php-mbstring \  
php7.0-mbstring \  
php-memcached \  
php-memcache \  
git \  
php7.0-zip \  
mysql-client  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN a2enmod rewrite ssl headers  
RUN mkdir /etc/apache2/ssl  
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout
/etc/apache2/ssl/app.key -out /etc/apache2/ssl/app.crt -subj /C=US/ST=New\
York/L=New\ York\ City/O=SuperDeveloper/OU=Developers/CN=localhost  
  
# Set the locale  
RUN apt-get clean && apt-get update && apt-get install -y locales  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV DATABASE_TYPE="mysqli" \  
MYSQL_HOST="localhost" \  
MYSQL_DATABASE_NAME="moodle" \  
MYSQL_PASSWORD="" \  
MYSQL_PORT_NUMBER="" \  
MYSQL_USER="root" \  
MOODLE_EMAIL="user@example.com" \  
MOODLE_LANGUAGE="en" \  
MOODLE_PASSWORD="bitnami" \  
MOODLE_SITENAME="New Site" \  
MOODLE_SITENAME_SHORT="New Site short" \  
MOODLE_USERNAME="admin" \  
YSU_HOST="localhost"  
## install composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
## install timezonedb  
RUN pecl install timezonedb  
RUN sed -i '$ a\extension=timezonedb.so' /etc/php/7.0/apache2/php.ini  
RUN sed -i '$ a\extension=timezonedb.so' /etc/php/7.0/cli/php.ini  
  
RUN a2dissite 000-default  
COPY app_vhost.conf /etc/apache2/sites-available/  
COPY app_vhost_ssl.conf /etc/apache2/sites-available/  
RUN rm -rf /etc/apache2/ports.conf  
COPY ports.conf /etc/apache2/  
RUN a2ensite app_vhost app_vhost_ssl  
  
RUN mkdir -p /usr/local/openssl/include/openssl/ && \  
ln -s /usr/include/openssl/evp.h /usr/local/openssl/include/openssl/evp.h && \  
mkdir -p /usr/local/openssl/lib/ && \  
ln -s /usr/lib/x86_64-linux-gnu/libssl.a /usr/local/openssl/lib/libssl.a && \  
ln -s /usr/lib/x86_64-linux-gnu/libssl.so /usr/local/openssl/lib/  
  
EXPOSE 80 443  
RUN mkdir /unison  
RUN mkdir -p /home/webapp  
  
RUN ln -s /unison /home/webapp/htdocs  
RUN mkdir /home/webapp/moodledata  
RUN chmod 0777 /home/webapp/moodledata  
RUN chown www-data -R /home/webapp  
RUN git clone \--depth=1 -b MOODLE_33_STABLE git://git.moodle.org/moodle.git
/unison  
COPY moodle-config.php /unison/config.php  
  
RUN chown -R root /home/webapp/htdocs  
RUN chmod -R 0755 /home/webapp/htdocs  
COPY app_start.sh /usr/local/bin/  
COPY moodle_db.sql /usr/local/bin/  
RUN chmod +x /usr/local/bin/app_start.sh  
CMD ["/usr/local/bin/app_start.sh"]

