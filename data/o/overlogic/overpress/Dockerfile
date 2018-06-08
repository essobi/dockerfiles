FROM wordpress:php7.0-fpm  
MAINTAINER Nik Ferios - OverLogic <contact@overlogic.gr>  
  
# install PHP extensions for OverPress  
RUN set -ex; \  
\  
apt-get update; \  
apt-get install -y \  
libicu-dev \  
libmcrypt-dev \  
libpspell-dev \  
libmagickwand-dev \  
&& pecl install imagick \  
&& docker-php-ext-enable imagick \  
&& docker-php-ext-install intl mcrypt pspell \  
&& rm -rf /var/lib/apt/lists/*  
  
# set recommended php settings for OverPress  
RUN { \  
echo 'memory_limit = 384M'; \  
echo 'file_uploads=On'; \  
echo 'upload_max_filesize=64M'; \  
echo 'post_max_size=64M'; \  
echo 'max_execution_time=600'; \  
echo 'max_input_vars=3000'; \  
} > /usr/local/etc/php/conf.d/overpress-recommended.ini  
  
# set recommended memory settings for OverPress  
# consider replacing this  
ADD op-config-sample /op-config-sample  
RUN sed -e '1r /op-config-sample' -i /usr/src/wordpress/wp-config-sample.php  
  
CMD ["php-fpm"]  

