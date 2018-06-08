FROM ubuntu:15.04  
# persistent / runtime deps  
RUN apt-get update && apt-get install -y ca-certificates curl libpcre3
librecode0 libsqlite3-0 libxml2 --no-install-recommends  
  
RUN apt-get install -y apache2 --no-install-recommends  
  
# install the PHP extensions we need  
RUN apt-get install -y libpng12-dev libjpeg-dev  
  
RUN apt-get install -y php5 php5-gd php5-cli php5-mysql libapache2-mod-php5
libapache2-mod-auth-mysql php5-mcrypt php5-xmlrpc php5-curl  
  
RUN apt-get install -y libphp-phpmailer libjs-prototype libjs-scriptaculous
tinymce libphp-snoopy libjs-jquery php-gettext libjs-cropper  
  
RUN rm -rf /var/www/html && mkdir -p /var/lock/apache2 /var/run/apache2
/var/log/apache2 /var/www/html && chown -R www-data:www-data /var/lock/apache2
/var/run/apache2 /var/log/apache2 /var/www/html  
  
# Apache + PHP requires preforking Apache for best results  
RUN a2dismod mpm_event && a2enmod mpm_prefork && a2enmod rewrite  
  
RUN mv /etc/apache2/apache2.conf /etc/apache2/apache2.conf.dist && rm
/etc/apache2/conf-enabled/* /etc/apache2/sites-enabled/*  
  
ENV GPG_KEYS 0BD78B5F97500D450838F95DFE857D9A90D90EC1
6E4F6AB321FDC07F2C332E3AC2BF0BC433CFC8B3  
RUN set -xe \  
&& for key in $GPG_KEYS; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV WORDPRESS_VERSION 4.3  
ENV WORDPRESS_SHA1 1e9046b584d4eaebac9e1f7292ca7003bfc8ffd7  
  
# upstream tarballs include ./wordpress/ so this gives us /usr/src/wordpress  
RUN curl -o wordpress.tar.gz -SL
https://wordpress.org/wordpress-${WORDPRESS_VERSION}.tar.gz \  
&& echo "$WORDPRESS_SHA1 *wordpress.tar.gz" | sha1sum -c - \  
&& tar -xzf wordpress.tar.gz -C /usr/src/ \  
&& rm wordpress.tar.gz \  
&& chown -R www-data:www-data /usr/src/wordpress  
  
COPY apache2.conf /etc/apache2/apache2.conf  
  
COPY apache2-foreground /usr/local/bin/  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
WORKDIR /var/www/html  
  
VOLUME /var/www/html  
  
EXPOSE 80 443  
# grr, ENTRYPOINT resets CMD now  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  

