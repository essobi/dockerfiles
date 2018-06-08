FROM wodby/drupal-mariadb  
MAINTAINER Yonas Yanfa <yonas@savaslabs.com>  
  
# Install packages  
RUN echo 'http://alpine.gliderlabs.com/alpine/edge/main' >
/etc/apk/repositories && \  
echo 'http://alpine.gliderlabs.com/alpine/edge/community' >>
/etc/apk/repositories && \  
echo 'http://alpine.gliderlabs.com/alpine/edge/testing' >>
/etc/apk/repositories && \  
  
apk add --update \  
libressl \  
curl \  
ca-certificates \  
php7 \  
php7-json \  
php7-phar \  
php7-iconv \  
php7-openssl \  
php7-curl \  
php7-mbstring \  
php7-dom \  
php7-xml \  
php7-bcmath \  
php7-zip \  
php7-bz2 \  
php7-zlib \  
php7-mcrypt \  
php7-sockets \  
php7-ctype \  
  
&& \  
# Update CA Certificates  
update-ca-certificates && \  
# Create symlinks for backward compatibility  
ln -sf /usr/bin/php7 /usr/bin/php && \  
# Install composer  
curl -sS https://getcomposer.org/installer | php7 -- --install-
dir=/usr/local/bin --filename=composer  
  
# Install Terminus  
RUN cd /tmp && \  
wget https://github.com/pantheon-systems/terminus/archive/0.13.x.zip && \  
unzip 0.13.x.zip && \  
cd ./terminus-0.13.x && \  
composer install && \  
ln -s /tmp/terminus-0.13.x/bin/terminus /usr/local/bin/terminus && \  
chmod 755 /usr/local/bin/terminus  
  
COPY terminus-setup.sh /tmp/  
COPY terminus-setup-mysqld.sh /tmp/  
  
WORKDIR /var/lib/mysql  
VOLUME /var/lib/mysql  
EXPOSE 3306  
  
CMD /tmp/terminus-setup.sh  

