FROM ubuntu:latest  
MAINTAINER Popsana Barida <popsyjunior@gmail.com>  
  
#Update apt-get repos  
RUN apt-get update -y  
  
#Install PHP, Apache2 and dependencies  
RUN apt-get -y install libapache2-mod-php7.0 php7.0 php7.0-cli php-xdebug
php7.0-mbstring sqlite3 php7.0-mysql php-imagick php-memcached php-pear curl
imagemagick php7.0-dev php7.0-phpdbg php7.0-gd npm nodejs-legacy php7.0-json
php7.0-curl php7.0-sqlite3 php7.0-intl php7.0-zip apache2 nano vim git-core
wget libsasl2-dev libssl-dev libsslcommon2-dev libcurl4-openssl-dev autoconf
g++ make openssl libssl-dev libcurl4-openssl-dev pkg-config libsasl2-dev
libpcre3-dev \  
&& a2enmod headers \  
&& a2enmod rewrite  
  
#Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN composer --version  
  
#Set Environment  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
RUN ln -sf /dev/stdout /var/log/apache2/access.log && \  
ln -sf /dev/stderr /var/log/apache2/error.log  
RUN mkdir -p $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR  
  
VOLUME [ "/var/www/html" ]  
WORKDIR /var/www/html  
  
# Install Cron  
#RUN apt-get install --assume-yes cron  
# Add crontab file in the cron directory  
#ADD crontab /etc/cron.d/animata-cron  
# Give execution rights on the cron job  
#RUN chmod a+x 0644 /etc/cron.d/animata-cron  
#RUN chmod a+x /etc/cron.d/animata-cron  
#RUN echo "* * * * * php /var/www/html/artisan schedule:run >> /dev/null 2>&1
>> /dev/null 2>&1" >> /etc/cron.d/animata-cron  
# Put the command in the crontab  
#RUN crontab /etc/cron.d/animata-cron  
#RUN cron  
#RUN cron status  
#Final Checks  
RUN service apache2 restart  
EXPOSE 80  
#EXPOSE 443  
ENTRYPOINT [ "/usr/sbin/apache2" ]  
CMD ["-D", "FOREGROUND"]  

