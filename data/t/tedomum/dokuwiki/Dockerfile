FROM php:apache  
  
WORKDIR /var/www/html  
  
RUN a2enmod rewrite  
  
COPY config/php.ini /usr/local/etc/php/  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends git \  
&& apt-get clean  
  
RUN rm -rf /var/www/html/*  
RUN curl -L -O http://download.dokuwiki.org/src/dokuwiki/dokuwiki-stable.tgz \  
&& tar --strip 1 -xzf dokuwiki-stable.tgz \  
&& rm dokuwiki-stable.tgz \  
&& rm -f COPYING VERSION README  
  
RUN tar -cf /data.tar data \  
&& tar -cf /conf.tar conf  
  
ADD htaccess .htaccess  
ADD ./start /start  
  
CMD ["/start"]  

