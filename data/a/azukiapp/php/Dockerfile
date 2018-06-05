FROM azukiapp/alpine:3.3  
MAINTAINER Ricardo Quintaniha <ricardo.aquintanilha@gmail.com>  
  
ENV PKG_NAME php  
  
RUN echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories;  
  
RUN apk add --update \  
${PKG_NAME} \  
${PKG_NAME}-cli \  
${PKG_NAME}-pdo \  
${PKG_NAME}-pdo_sqlite \  
${PKG_NAME}-pdo_mysql \  
${PKG_NAME}-pdo_pgsql \  
${PKG_NAME}-redis@testing \  
${PKG_NAME}-memcached@testing \  
${PKG_NAME}-json \  
${PKG_NAME}-openssl \  
${PKG_NAME}-dev \  
${PKG_NAME}-curl \  
${PKG_NAME}-mcrypt \  
${PKG_NAME}-dom \  
${PKG_NAME}-intl \  
${PKG_NAME}-ctype \  
${PKG_NAME}-gd \  
${PKG_NAME}-dom \  
${PKG_NAME}-intl \  
${PKG_NAME}-ctype \  
${PKG_NAME}-gd \  
${PKG_NAME}-iconv \  
${PKG_NAME}-xsl \  
${PKG_NAME}-zip \  
${PKG_NAME}-phar \  
${PKG_NAME}-xdebug@testing \  
&& rm -rf /var/cache/apk/* /var/tmp/* /tmp/*  
  
RUN sed -i 's/display_errors = Off/display_errors = On/g' /etc/php/php.ini \  
&& sed -i 's/extension/zend_extension/g' /etc/php/conf.d/xdebug.ini  
  
RUN php -r "readfile('https://getcomposer.org/installer');" > composer-
setup.php \  
&& php composer-setup.php --install-dir=/usr/local/bin --filename=composer \  
&& php -r "unlink('composer-setup.php');"  
  
CMD ["php", "-a"]  

