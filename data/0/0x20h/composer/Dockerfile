FROM alpine:edge  
MAINTAINER Jan Kohlhof <kohj@informatik.uni-marburg.de>  
  
RUN apk --no-cache git php7 php7-curl php7-openssl php7-json php7-phar
php7-pdo php7-dom php7-mbstring php7-zlib git && \  
rm /var/cache/apk/* && \  
ln -s /usr/bin/php7 /usr/bin/php && \  
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \  
php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" && \  
php composer-setup.php --install-dir=/usr/bin --filename=composer && \  
php -r "unlink('composer-setup.php');"  
  
WORKDIR /project  
COPY startup.sh /usr/local/bin  
ENTRYPOINT ["/usr/local/bin/startup.sh"]  

