FROM mdjw866/php-fpm:latest  
MAINTAINER M.D.Ward <dev@mattdw.co.uk>  
  
RUN pecl install xdebug-2.4.0 && \  
echo "zend_extension=$(ls -1 /usr/local/lib/php/extensions/*/xdebug.so)" >
/usr/local/etc/php/conf.d/xdebug.ini  
  
ADD php-fpm.sh /php-fpm.sh  
  
RUN chmod +x /php-fpm.sh  
  
CMD ["/php-fpm.sh"]  

