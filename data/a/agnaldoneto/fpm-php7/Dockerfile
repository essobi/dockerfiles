FROM php:7.2-rc-fpm  
MAINTAINER Agnaldo Marinho <agnaldomarinho7@gmail.com> (@agnaldo_nm)  
  
# Disable remote database security requirements.  
ENV JOOMLA_INSTALLATION_DISABLE_LOCALHOST_CHECK=1  
# Install PHP extensions  
RUN apt-get update && apt-get install -y libpng-dev git libjpeg-dev libmcrypt-
dev zip unzip && rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd  
RUN docker-php-ext-install mysqli  
RUN docker-php-ext-install zip  
  
VOLUME /var/www/html  
  
# Download package JoomlaGov  
RUN git clone https://github.com/joomlagovbr/joomla-3.x.git /var/www/html  
  
# Copy init scripts and custom .htaccess  
COPY docker-entrypoint.sh /entrypoint.sh  
COPY makedb.php /makedb.php  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["php-fpm"]  

