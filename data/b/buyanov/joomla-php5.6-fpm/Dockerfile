FROM php:5.6-fpm  
  
# install the PHP extensions we need  
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev && rm -rf
/var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd  
RUN docker-php-ext-install mysqli  
  
WORKDIR /var/www/html  
  
ENV JOOMLA_VERSION 3.4.4  
ENV JOOMLA_SHA1 a95ce2f90d20953fc252abb6b8aa7a87e82bd421  
ENV JOOMLA_URL https://github.com/joomla/joomla-
cms/releases/download/${JOOMLA_VERSION}/Joomla_${JOOMLA_VERSION}-Stable-
Full_Package.tar.gz  
  
RUN curl -o joomla.tar.gz -SL ${JOOMLA_URL} \  
&& echo "$JOOMLA_SHA1 joomla.tar.gz" | sha1sum -c - \  
&& tar -xzf joomla.tar.gz -C /var/www/html/ \  
&& rm joomla.tar.gz \  
&& chown -R www-data:www-data /var/www/html  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stderr /var/log/php5-fpm.log  
  
VOLUME /var/www/html  
  
CMD ["php-fpm"]  

