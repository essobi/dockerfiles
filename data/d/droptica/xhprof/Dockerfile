FROM droptica/drupal-apache:7  
  
RUN apt-get update && apt-get -y install unzip graphviz  
  
RUN curl -L -o xhprof.zip https://github.com/RustJason/xhprof/archive/php7.zip
\  
&& unzip xhprof.zip \  
&& rm xhprof.zip \  
&& mv xhprof-php7/* /var/www \  
&& rm -rf /var/www/html \  
&& mv /var/www/xhprof_html /var/www/html \  
&& cd /var/www/extension \  
&& phpize \  
&& ./configure --enable-xhprof \  
&& make \  
&& make install  
  
ADD xhprof.ini /usr/local/etc/php/conf.d/xhprof.ini

