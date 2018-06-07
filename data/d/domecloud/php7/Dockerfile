FROM domecloud/openresty:edge  
MAINTAINER Dome C. <dome@tel.co.th>  
  
COPY start.sh /start.sh  
RUN chmod +x /start.sh  
COPY /conf /opt/lixen/nginx/conf/  
COPY info.php /opt/lixen/nginx/html  
  
# Add PHP 7  
RUN echo 'http://nl.alpinelinux.org/alpine/edge/testing' >>
/etc/apk/repositories && \  
apk upgrade -U && \  
apk --update --repository=http://dl-4.alpinelinux.org/alpine/edge/testing
--repository=http://dl-4.alpinelinux.org/alpine/edge/community add curl bash \  
php7 \  
php7-xml \  
php7-xsl \  
php7-pdo_mysql \  
php7-mcrypt \  
php7-curl \  
php7-json \  
php7-fpm \  
php7-phar \  
php7-openssl \  
php7-mysqli \  
php7-ctype \  
php7-opcache \  
php7-mbstring php7-zip php7-redis php7-gd redis mini-sendmail php7-mongodb  
  
RUN ln -s /etc/php7 /etc/php && \  
ln -s /usr/sbin/php-fpm7 /usr/bin/php-fpm && \  
ln -s /usr/lib/php7 /usr/lib/php && \  
rm -fr /var/cache/apk/*  
RUN adduser -D -H -h /opt/lixen/nginx/html www-data  
RUN chown www-data.www-data -R /opt/lixen/nginx/html/  
RUN sed -i "s/user = nobody/user = www-data/g" /etc/php7/php-fpm.d/www.conf  
RUN sed -i "s/group = nobody/group = www-data/g" /etc/php7/php-fpm.d/www.conf  
  
# Install composer global bin  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
ENV TERM screen-256color  
ENV SHELL=/bin/bash  
  
EXPOSE 80 443  
ENTRYPOINT ["/start.sh"]  

