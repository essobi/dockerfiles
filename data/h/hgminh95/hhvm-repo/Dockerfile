FROM diegomarangoni/hhvm  
  
MAINTAINER hgminh95@gmail.com  
  
COPY php.ini /etc/hhvm/php.ini  
  
COPY hhvm_entrypoint.sh /usr/local/bin/  
  
ENV PHP_SRC_ROOT /var/www/html  
  
EXPOSE 9000  
ENTRYPOINT ["hhvm_entrypoint.sh"]  
CMD ["hhvm", "--mode", "server", "--config", "/etc/hhvm/php.ini"]  

