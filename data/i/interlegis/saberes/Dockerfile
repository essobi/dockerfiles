FROM alpine:3.6  
MAINTAINER Matheus Garcia <garcia.figueiredo@gmail.com>  
MAINTAINER Fabio Rauber <fabiorauber@gmail.com>  
  
ENV MOODLE_VERSION=32 \  
MOODLE_GITHUB=https://github.com/interlegis/moodle.git \  
MOODLE_DATA=/var/moodledata \  
MOODLE_REVERSEPROXY=false \  
MOODLE_SSLPROXY=false \  
SABERES_VERSION=3.2.1-50  
EXPOSE 80  
VOLUME ["/var/moodledata"]  
  
RUN apk update \  
&& apk add --no-cache \  
dcron \  
git \  
apache2 \  
php7 \  
php7-apache2 \  
php7-iconv \  
php7-pgsql \  
php7-session \  
php7-json \  
php7-xml \  
php7-curl \  
php7-zip \  
php7-zlib \  
php7-gd \  
php7-dom \  
php7-xmlreader \  
php7-mbstring \  
php7-openssl \  
php7-xmlrpc \  
php7-soap \  
php7-intl \  
php7-opcache \  
php7-tokenizer \  
php7-simplexml \  
php7-ctype  
  
RUN cd /tmp \  
&& git clone ${MOODLE_GITHUB} \--depth=1 --branch ${SABERES_VERSION} \  
&& rm -rf /var/www/localhost/htdocs \  
&& mv /tmp/moodle /var/www/localhost/htdocs \  
&& chown apache:apache -R /var/www/localhost/htdocs \  
&& mkdir /run/apache2  
  
RUN ln -sf /proc/self/fd/1 /var/log/apache2/access.log \  
&& ln -sf /proc/self/fd/1 /var/log/apache2/error.log  
  
COPY moodle-config.php /var/www/localhost/htdocs/config.php  
COPY 00_limits.ini /etc/php7/conf.d/00_limits.ini  
COPY 00_opcache.ini /etc/php7/conf.d/00_opcache.ini  
COPY run.sh /opt/apache2/run.sh  
COPY crontab /etc/crontabs/root  
COPY startcron.sh /usr/local/bin  
  
CMD ["/opt/apache2/run.sh"]  

