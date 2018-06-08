FROM wordpress:php5.6-apache  
  
RUN { \  
echo 'post_max_size=50M'; \  
echo 'upload_max_filesize=50M'; \  
} > "$PHP_INI_DIR/php.ini"  

