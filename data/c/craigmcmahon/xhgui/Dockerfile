FROM craigmcmahon/apache-php:v1.2.0  
  
ENV XHGUI_TAG="v0.7.1"  
RUN apk --no-cache --repository
http://dl-4.alpinelinux.org/alpine/edge/testing add \  
php7-mongodb \  
php7-phar  
RUN apk --no-cache add git \  
&& mkdir /app \  
&& cd /app \  
&& git clone https://github.com/perftools/xhgui.git \  
&& cd xhgui \  
&& git checkout tags/${XHGUI_TAG} \  
&& /usr/bin/php install.php \  
&& apk del git \  
&& rm -rf /var/www \  
&& mv /app/xhgui /var/www \  
&& chmod 777 /var/www/cache  
COPY config.php /var/www/config/config.php  
COPY apache-config.conf /etc/apache2/conf.d/custom/xhgui.conf

