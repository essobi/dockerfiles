FROM alpine:3.6  
LABEL maintainer="s@pax.so"  
  
RUN \  
# sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories
&& \  
apk add --update --no-cache dcron wget tzdata php7 php7-opcache php7-curl
php7-json php7-phar php7-mbstring php7-zlib php7-openssl php7-pcntl && \  
EXPECTED_COMPOSER_SIGNATURE=$(wget -q -O -
https://composer.github.io/installer.sig) && \  
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \  
php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'${EXPECTED_COMPOSER_SIGNATURE}') { echo 'Composer.phar Installer verified'; }
else { echo 'Composer.phar Installer corrupt'; unlink('composer-setup.php'); }
echo PHP_EOL;" && \  
php composer-setup.php --install-dir=/usr/bin --filename=composer && \  
php -r "unlink('composer-setup.php');" && \  
cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \  
echo "Asia/Shanghai" > /etc/timezone && \  
crontab -l | { cat; echo "0 */8 * * * php /data/get_radar_pics.php"; } |
crontab - && \  
mkdir /data  
  
ADD composer.* /data/  
ADD get_radar_pics.php /data/  
  
RUN composer install --prefer-dist --no-progress --no-interaction --working-
dir=/data  
  
CMD crond -fS  

