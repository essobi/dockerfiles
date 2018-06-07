FROM lacquerlabs/service-php7:latest  
  
# Wordpress Specific ENV Vars  
ENV DB_CHARSET utf8mb4  
# ENV DB_COLLATE ""  
ENV AUTH_KEY setme_AUTH_KEY  
ENV SECURE_AUTH_KEY setme_SECURE_AUTH_KEY  
ENV LOGGED_IN_KEY setme_LOGGED_IN_KEY  
ENV NONCE_KEY setme_NONCE_KEY  
ENV AUTH_SALT setme_AUTH_SALT  
ENV SECURE_AUTH_SALT setme_SECURE_AUTH_SALT  
ENV LOGGED_IN_SALT setme_LOGGED_IN_SALT  
ENV NONCE_SALT setme_NONCE_SALT  
ENV WP_DEBUG false  
ENV WP_TABLE_PREFIX wp2_  
  
ENV WP_VERSION 4.8.1  
# install database and other needed packages for wordpress  
# Remove php7-zlib as it now resides in php7  
RUN apk --update --no-cache add php7-mysqli php7-imagick openssl  
  
# fix root path for nginx  
# RUN sed -i "s|.*root.*/app;| root /app/wordpress;|i"
/etc/nginx/conf.d/default.conf  
# copy wp-config.php to wordpress directory, will be owned by root.  
COPY ./configs/wp-config.php /app/wp-config.php  
  
# download and set the user/group pair for wordpress  
RUN wget -O /tmp/wordpress.tgz
https://wordpress.org/wordpress-${WP_VERSION}.tar.gz && \  
tar -zxvf /tmp/wordpress.tgz --directory /app --strip-components=1 && \  
apk del openssl && \  
rm /tmp/wordpress.tgz && \  
chown -R www-data:www-data /app  
  

