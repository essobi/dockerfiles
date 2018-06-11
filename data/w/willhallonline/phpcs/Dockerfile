FROM willhallonline/composer  
  
# Install PHPCS  
RUN composer global require "squizlabs/php_codesniffer=2.9"  
  
WORKDIR /app  
  
CMD ["phpcs"]  
CMD ["phpcbf"]  

