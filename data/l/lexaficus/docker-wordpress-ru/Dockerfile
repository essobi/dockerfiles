FROM ubuntu:14.04  
MAINTAINER lexaficus  
  
RUN apt-get update && apt-get install -y rsync && rm -r /var/lib/apt/lists/*  
  
RUN apt-get update && apt-get install -y php5 php5-cli php5-dev php5-fpm
php5-cgi php5-mysql php5-xmlrpc php5-curl php5-gd php-apc php-pear php5-imap
php5-mcrypt php5-pspell php5-imagick nginx libssh2-php  
  
VOLUME /var/www/html  
  
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g"
/etc/php5/fpm/php.ini  
RUN sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
/etc/php5/fpm/php.ini  
RUN sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g"
/etc/php5/fpm/php.ini  
  
ENV WORDPRESS_VERSION 4.1.0  
ENV WORDPRESS_UPSTREAM_VERSION 4.1  
ENV WORDPRESS_MD5 9549a510b2710a6ea92d80918e63623b  
  
RUN cd /var/www/html  
  
# upstream tarballs include ./wordpress/ so this gives us /usr/src/wordpress  
RUN curl -o wordpress.tar.gz -SL
https://ru.wordpress.org/wordpress-${WORDPRESS_UPSTREAM_VERSION}-ru_RU.tar.gz
\  
&& echo "$WORDPRESS_MD5 *wordpress.tar.gz" | md5sum -c - \  
&& tar -xzf wordpress.tar.gz -C /usr/src/ \  
&& rm wordpress.tar.gz  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
RUN rm /etc/nginx/sites-available/default  
COPY nginx.conf /etc/nginx/sites-available/default  
  
# grr, ENTRYPOINT resets CMD now  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 80  
COPY start.sh /start.sh  
CMD ["/start.sh"]

