FROM alpine:3.3  
#Install grav into /www folder  
RUN apk --update add nginx php-fpm wget curl git zip unzip php php-curl php-
zip php-openssl php-json php-phar php-dom php-gd php-ctype php-xml && \  
rm /var/cache/apk/* && \  
curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer && \  
mkdir /www && cd /www && \  
git clone -b master https://github.com/getgrav/grav.git . && \  
bin/grav install && \  
chown -R nobody . && chown -R nobody * && \  
find . -type f | xargs chmod 664 && \  
find ./bin -type f | xargs chmod 775 && \  
find . -type d | xargs chmod 775 && \  
find . -type d | xargs chmod +s && \  
umask 0002 && \  
mkdir -p /var/log/nginx && \  
touch /var/log/nginx/access.log && \  
mkdir -p /tmp/nginx && \  
echo "clear_env = no" >> /etc/php/php-fpm.conf  
  
#Add nginx and php-fpm configuration  
ADD etc /etc  
EXPOSE 80  
#Start nginx and php-fpm  
CMD php-fpm -d variables_order="EGPCS" && (tail -F /var/log/nginx/access.log
&) && exec nginx -g "daemon off;"  

