ARG PHP_VER=7.2  
FROM wordpress:php${PHP_VER}-apache  
MAINTAINER Sebastian Plocek <sebastian@plocek.at>  
  
ARG PHP_VER  
  
# Increase Upload and Memory Limit  
RUN echo "file_uploads = On\n" \  
"memory_limit = 512M\n" \  
"upload_max_filesize = 128M\n" \  
"post_max_size = 128M\n" \  
"max_execution_time = 600\n" \  
> /usr/local/etc/php/conf.d/custom-limits.ini  
  
# Increase Memory Limit for Wordpress  
RUN sed \  
-i "/MySQL settings/idefine( 'WP_MEMORY_LIMIT', '128M' );" \  
/usr/src/wordpress/wp-config-sample.php  
  
# Add PHP Zip Archive extension  
RUN apt-get update \  
&& apt-get install -y zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install zip

