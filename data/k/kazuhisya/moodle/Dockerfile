# vi: set ft=dockerfile :  
FROM alpine:3.6  
  
ENV TZ="Asia/Tokyo" \  
MOODLE_VERSION="stable33" \  
MOODLE_TAG="latest-33"  
  
RUN apk --update add \  
apache2 \  
bash \  
curl \  
php7 \  
php7-apache2 \  
php7-apcu \  
php7-ctype \  
php7-curl \  
php7-dom \  
php7-fileinfo \  
php7-gd \  
php7-iconv \  
php7-intl \  
php7-json \  
php7-mbstring \  
php7-opcache \  
php7-openssl\  
php7-pgsql \  
php7-session \  
php7-simplexml \  
php7-soap \  
php7-tokenizer \  
php7-xmlreader \  
php7-xmlrpc \  
php7-zip \  
php7-zlib \  
postgresql-client && \  
rm -f /var/cache/apk/*  
  
WORKDIR /var/www/localhost/htdocs  
  
RUN curl -OL
https://download.moodle.org/${MOODLE_VERSION}/moodle-${MOODLE_TAG}.tgz && \  
tar xf moodle-${MOODLE_TAG}.tgz && \  
rm -rf moodle-${MOODLE_TAG}.tgz  
  
RUN mkdir -p /var/www/moodledata && \  
echo "date.timezone = '${TZ}'\n" > /etc/php7/conf.d/timezone.ini && \  
sed -ri \  
-e 's!^(\s*CustomLog)\s+\S+!\1 /proc/self/fd/1!g' \  
-e 's!^(\s*ErrorLog)\s+\S+!\1 /proc/self/fd/2!g' \  
"/etc/apache2/httpd.conf"  
  
COPY src/config.php /var/www/localhost/htdocs/moodle/config.php  
COPY src/index.html /var/www/localhost/htdocs/index.html  
COPY src/start.sh /root/start.sh  
  
CMD /root/start.sh  

