FROM ipropertygroup/webserver:nginx-php56-31  
MAINTAINER MOHSEN@IPROPERTY  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# install the PHP extensions we need  
RUN apt-get clean && apt-get update --fix-missing  
RUN apt-get install -y libmemcached-dev libpng12-dev libjpeg-dev git curl zip
unzip \  
&& rm -rf /var/lib/apt/lists/* \  
&& pecl install memcache \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mysqli opcache\  
&& docker-php-ext-enable memcache opcache\  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# install NewRelic  
ENV NR_INSTALL_SILENT true  
ENV NEWRELIC_LICENSE **None**  
RUN curl -sL https://download.newrelic.com/548C16BF.gpg | apt-key add - \  
&& sh -c 'echo "deb http://apt.newrelic.com/debian/ newrelic non-free" >
/etc/apt/sources.list.d/newrelic.list' \  
&& apt-get update \  
&& apt-get install -y newrelic-php5 \  
&& apt-get clean \  
&& newrelic-install install

