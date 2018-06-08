FROM alpine:3.6  
  
ENV BASE_PACKAGES="php5-common php5-fpm" \  
ADDITIONAL_PACKAGES="php5-pear php5-json php5-xml"  
  
RUN apk update && \  
apk add \--no-cache --no-progress \  
$BASE_PACKAGES $ADDITIONAL_PACKAGES && \  
rm -rfv /var/cache/apk/* && \  
printf '[global]\n' > /etc/php5/php-fpm.conf && \  
printf 'error_log = /var/log/php-fpm.log\n' >> /etc/php5/php-fpm.conf && \  
printf '[www]\n' >> /etc/php5/php-fpm.conf && \  
printf 'user = digitalnbcu\n' >> /etc/php5/php-fpm.conf && \  
printf 'group = digitalnbcu\n' >> /etc/php5/php-fpm.conf && \  
printf 'listen = 127.0.0.1:9000\n' >> /etc/php5/php-fpm.conf && \  
printf 'pm = dynamic\n' >> /etc/php5/php-fpm.conf && \  
printf 'pm.max_children = 5\n' >> /etc/php5/php-fpm.conf && \  
printf 'pm.start_servers = 2\n' >> /etc/php5/php-fpm.conf && \  
printf 'pm.min_spare_servers = 1\n' >> /etc/php5/php-fpm.conf && \  
printf 'pm.max_spare_servers = 3\n' >> /etc/php5/php-fpm.conf && \  
sed -i -e 's/short_open_tag\ \=\ Off/short_open_tag\ \=\ On/g' \  
/etc/php5/php.ini  
  
EXPOSE 9000  
  
CMD ["php-fpm", "-F"]  
  

