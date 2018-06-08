FROM easytek/nginx-php  
  
RUN apt-get -qq update && DEBIAN_FRONTEND=noninteractive apt-get -qq -y --no-
install-recommends install \  
php5-gd \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD docker/vhost.conf /etc/nginx/sites-enabled/default  
ADD . /var/www  
  
RUN composer install

