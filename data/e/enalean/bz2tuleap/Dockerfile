FROM alpine:3.7 as builder  
  
RUN apk add --no-cache php7 php7-openssl php7-dom php7-xmlreader php7-json
php7-phar php7-mbstring ca-certificates && \  
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \  
php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" && \  
php composer-setup.php --install-dir=/usr/bin/ --filename=composer && \  
php -r "unlink('composer-setup.php');"  
  
COPY . /app  
  
WORKDIR /app/  
  
RUN composer install --no-dev -a  
  
FROM alpine:3.7  
RUN apk add --no-cache php7 php7-openssl php7-dom php7-simplexml
php7-xmlreader ca-certificates  
  
WORKDIR /app/  
  
COPY \--from=builder /app .  
  
CMD [ "sh", "/app/help.sh" ]  

