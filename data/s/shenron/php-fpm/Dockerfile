FROM shenron/php-fpm:7.2  
  
RUN echo "zend_extension=$(php-config --extension-dir)/xdebug.so" >>
/usr/local/etc/php/php.ini && \  
sed -i "s/opcache.revalidate_freq=60/opcache.revalidate_freq=0/"
/usr/local/etc/php/php.ini &&\  
sed -i "s/opcache.save_comments/; opcache.save_comments/"
/usr/local/etc/php/php.ini  

