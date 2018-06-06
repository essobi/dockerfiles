FROM wordpress:4.7.2-fpm  
  
MAINTAINER Javier Jerónimo <jcjeronimo@genexies.net>  
  
#  
# @param[in] REPOSITORIES Git repositories to clone (each: https including  
# credentials in URL)  
#  
# @param[in] ADDITIONAL_TARGZ_URLS Additional Tar.Gz files URLs to download
and uncompress in /var/www/html  
#  
# @param[in] DEBUG If present, all debug options are enabled in  
# Wordpress  
#  
# Required to install libapache2-mod-fastcgi  
RUN echo "deb http://http.us.debian.org/debian jessie main non-free" >>
/etc/apt/sources.list  
  
RUN apt-get update && apt-get install -y \  
supervisor \  
git \  
wget \  
php-pear \  
sudo \  
apache2 \  
php5-fpm \  
apache2-mpm-event \  
libapache2-mod-fastcgi \  
curl \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY etc/supervisor/conf.d/supervisord.conf
/etc/supervisor/conf.d/supervisord.conf  
  
# Install OPcache  
RUN docker-php-ext-install opcache  
COPY opcache.ini /opcache.ini  
RUN cat /opcache.ini >> /usr/local/etc/php/conf.d/docker-php-ext-opcache.ini  
  
# Download manually, and install using PHP docker scripts...  
WORKDIR /usr/src/php/ext  
RUN wget https://pecl.php.net/get/memcache-2.2.7.tgz && \  
tar xvzf memcache-2.2.7.tgz && \  
mv memcache-2.2.7 memcache  
RUN docker-php-ext-configure memcache && docker-php-ext-install memcache  
ENV APPLICATION_PATH /var/www/html  
WORKDIR ${APPLICATION_PATH}  
  
COPY etc/apache2/apache2.conf /etc/apache2/apache2.conf  
COPY usr/local/etc/php-fpm.conf /usr/local/etc/php-fpm.conf  
  
RUN a2enmod mpm_event  
  
# Apache's module to communicate with FastCGI process: fastcgi  
COPY etc/apache2/conf-available/fastcgi.conf /etc/apache2/conf-
available/fastcgi.conf  
RUN a2enconf fastcgi  
  
# Enable Apache modules  
RUN a2enmod rewrite actions  
  
# Our entry-point that fallback to parent's  
COPY gnx-entrypoint.sh /gnx-entrypoint.sh  
RUN chmod u+x /gnx-entrypoint.sh  
ENTRYPOINT ["/gnx-entrypoint.sh"]  
  
ENV REPOSITORIES=  
ENV ADDITIONAL_TARGZ_URLS=  
ENV DEBUG=  
  
EXPOSE 80  
# Same default parameter to parent's entry-point  
CMD ["/usr/bin/supervisord"]  

