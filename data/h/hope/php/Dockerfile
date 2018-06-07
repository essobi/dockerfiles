FROM hope/base-alpine:3.5  
  
ENV \  
PHP_VERSION=7.1.5 \  
PHP_CONFIG=/etc/php7/php.ini \  
FPM_CONFIG=/etc/php7/php-fpm.d/www.conf  
  
RUN \  
# Install  
apk add --no-cache \  
php7@edge \  
php7-fpm@edge \  
php7-mongodb@edge \  
php7-pdo@edge \  
php7-mysqlnd@edge \  
php7-mysqli@edge \  
php7-xml@edge \  
php7-dom@edge \  
php7-simplexml@edge \  
php7-json@edge \  
php7-gd@edge \  
php7-opcache@edge \  
php7-iconv@edge \  
php7-mbstring@edge \  
php7-curl@edge \  
php7-ctype@edge \  
php7-zlib@edge \  
php7-openssl@edge \  
php7-session@edge \  
php7-tokenizer@edge \  
php7-phar@edge \  
php7-posix@edge \  
php7-pcntl@edge && \  
# Configure  
sed -i -e "s/listen = 127.0.0.1:9000/listen = 0.0.0.0:9000/g" ${FPM_CONFIG} &&
\  
sed -i -e "s/user = nobody/user = root/g" ${FPM_CONFIG} && \  
sed -i -e "s/group = nobody/group = root/g" ${FPM_CONFIG} && \  
  
sed -i -e "s/;date.timezone =/date.timezone = Europe\/Kiev/g" ${PHP_CONFIG} &&
\  
sed -i -e "s/upload_max_filesize = 2M/upload_max_filesize = 100M/g"
${PHP_CONFIG} && \  
sed -i -e "s/post_max_size = 8M/post_max_size = 100M/g" ${PHP_CONFIG} && \  
# Install Composer  
cd /tmp && \  
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \  
php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" && \  
php composer-setup.php && \  
php -r "unlink('composer-setup.php');" && \  
mv composer.phar /usr/bin/composer && \  
# Log redirect  
ln -sf /dev/stdout /var/log/php-fpm.log  
  
EXPOSE 9000  
  
ENTRYPOINT ["php-fpm7", "--nodaemonize", "--allow-to-run-as-root"]  

