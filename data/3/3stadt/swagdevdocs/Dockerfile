FROM php:7.1-alpine  
  
ADD php/_010_php.ini /usr/local/etc/php/conf.d/  
  
RUN apk add \--no-cache freetype libpng libjpeg-turbo freetype-dev libpng-dev
libjpeg-turbo-dev git bash bash-completion \  
&& docker-php-ext-configure gd \  
\--with-gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
&& NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \  
&& docker-php-ext-install -j${NPROC} gd \  
&& apk del --no-cache freetype-dev libpng-dev libjpeg-turbo-dev  
  
RUN adduser -D -u 1000 dev \  
&& mkdir -p /home/dev  
  
ENV HOME /home/dev  
  
RUN chown -R dev: /home/dev  
USER dev  
  
WORKDIR /home/dev  
  
ENTRYPOINT ["bash"]

