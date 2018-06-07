FROM debian:9.2  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
  
# install apache2 + php  
RUN echo "Europe/Paris" > /etc/timezone && \  
dpkg-reconfigure tzdata && \  
apt-get -y update && \  
apt-get -y upgrade && \  
apt-get -y install \  
apache2 \  
libapache2-mod-php7.0 \  
curl \  
git \  
php7.0-dom \  
unzip  
  
COPY gitlist.conf /etc/apache2/conf-available/gitlist.conf  
  
RUN a2enmod cgi  
  
# install gitlist  
RUN (cd /var/www/html/ && \  
curl -0 https://codeload.github.com/klaussilveira/gitlist/tar.gz/0.5.0 | tar
-zx) && \  
(cd /var/www/html/ && ln -s gitlist-0.5.0 gitlist && cd gitlist && \  
mv config.ini-example config.ini && \  
chmod a+rwx cache/) && \  
(cd /home/ && \  
mkdir -p /home/git/repositories/) && \  
a2enmod rewrite && \  
ln -s /etc/apache2/conf-available/gitlist.conf /etc/apache2/conf-
enabled/gitlist.conf  
  
RUN cd /var/www/html/gitlist && \  
curl -sS https://getcomposer.org/installer | php && \  
php composer.phar --optimize-autoloader --classmap-authoritative --no-dev
--prefer-dist install  
  
# repositories folder  
VOLUME /home/git/repositories/  
EXPOSE 80  
# forward request and error logs to docker log collector  
RUN ln -sf /proc/1/fd/1 $APACHE_LOG_DIR/access.log \  
&& ln -sf /proc/1/fd/1 $APACHE_LOG_DIR/error.log \  
&& ln -sf /proc/1/fd/1 "$APACHE_LOG_DIR/other_vhosts_access.log"  
  
RUN sed -i -e "s/ServerTokens OS/ServerTokens prod/g" /etc/apache2/conf-
available/security.conf  
  
Run sed -i -e "s/ErrorLog \${APACHE_LOG_DIR}\/error.log/ErrorLog
\/dev\/null/g" /etc/apache2/apache2.conf  
  
CMD ["apache2", "-D", "FOREGROUND"]  

