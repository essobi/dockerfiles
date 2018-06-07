FROM ridibooks/performance-apache-base:7.1  
MAINTAINER Kang Ki Tae <kt.kang@ridi.com>  
  
ENV APACHE_DOC_ROOT /var/www/html/web  
  
# Install zip, cron and PHP modules (gd, exif)  
RUN apt-get update \  
&& apt-get install -y \  
zip cron libfreetype6-dev libjpeg62-turbo-dev libpng12-dev libxpm-dev libvpx-
dev \  
&& docker-php-ext-configure gd \  
\--with-freetype-dir=/usr/lib/x86_64-linux-gnu/ \  
\--with-jpeg-dir=/usr/lib/x86_64-linux-gnu/ \  
\--with-png-dir=/usr/lib/x86_64-linux-gnu/ \  
\--with-xpm-dir=/usr/lib/x86_64-linux-gnu/ \  
\--with-vpx-dir=/usr/lib/x86_64-linux-gnu/ \  
&& docker-php-ext-install gd exif \  
  
# Clean  
&& apt-get autoclean -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*  
  
# Set PHP custom config  
ADD docs/docker/php/* /usr/local/etc/php/conf.d/  
  
# Set cron  
ADD docs/docker/cron.d/intranet_crontab /etc/cron.d/  
  
# Change entrypoint  
EXPOSE 80 443  
ADD docs/docker/docker-intranet-entrypoint.sh /  
ENTRYPOINT ["/docker-intranet-entrypoint.sh"]  
CMD ["apache2-foreground"]  
  
ADD . /var/www/html  
WORKDIR /var/www/html  
RUN chown -R www-data:www-data /var/www/html/var \  
&& chmod 755 /var/www/html/var  
  
RUN make  

