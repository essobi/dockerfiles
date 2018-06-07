FROM wordpress  
  
LABEL maintainer="Michal Idziorek <m.i@gmx.at>"  
  
RUN apt-get update && apt-get install -y sendmail libpng-dev libfreetype6-dev
&& \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ && \  
docker-php-ext-install gd && \  
a2enmod remoteip  
  
COPY ./php.ini /usr/local/etc/php/conf.d/php.ini  
COPY ./uploads.ini /usr/local/etc/php/conf.d/uploads.ini  
COPY ./start.sh /start.sh  
  
ENTRYPOINT [""]  
CMD ["/start.sh"]  

