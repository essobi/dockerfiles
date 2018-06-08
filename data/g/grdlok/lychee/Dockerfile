FROM alpine  
LABEL maintainer="adam@hello-world.ca"  
  
# Environment Variables  
ENV PHP_FPM_USER "www"  
ENV PHP_FPM_GROUP "www"  
ENV PHP_FPM_LISTEN_MODE "0660"  
ENV PHP_MAX_EXEC_TIME "200"  
ENV PHP_POST_MAX_SIZE "100M"  
ENV PHP_UPLOAD_MAX_SIZE "100M"  
ENV PHP_UPLOAD_MAX_FILESIZE "20M"  
ENV PHP_MEMORY_LIMIT "256M"  
ENV PHP_DISPLAY_ERRORS "On"  
ENV PHP_DISPLAY_STARTUP_ERRORS "On"  
ENV PHP_ERROR_REPORTING
"E_COMPILE_ERROR\|E_RECOVERABLE_ERROR\|E_ERROR\|E_CORE_ERROR"  
ENV PHP_CGI_FIX_PATHINFO "0"  
  
# Copy Over Configuration Files  
COPY ./nginx.conf ./  
COPY ./supervisord.conf ./  
  
# Install Packages  
RUN apk -U upgrade \  
&& apk add git nodejs nginx openrc supervisor \  
php5 php5-common php5-cli php5-mysql \  
php5-fpm php5-json php5-zip php5-gd php5-exif \  
php5-mcrypt php5-mysqli  
  
# PHP FPM Update Config  
# https://wiki.alpinelinux.org/wiki/Nginx_with_PHP#Nginx_with_PHP  
RUN sed -i "s|;listen.owner\s*=\s*nobody|listen.owner = ${PHP_FPM_USER}|g"
/etc/php5/php-fpm.conf \  
&& sed -i "s|;listen.group\s*=\s*nobody|listen.group = ${PHP_FPM_GROUP}|g"
/etc/php5/php-fpm.conf \  
&& sed -i "s|;listen.mode\s*=\s*0660|listen.mode = ${PHP_FPM_LISTEN_MODE}|g"
/etc/php5/php-fpm.conf \  
&& sed -i "s|user\s*=\s*nobody|user = ${PHP_FPM_USER}|g" /etc/php5/php-
fpm.conf \  
&& sed -i
"s|include\s*=\s*\/etc\/php5\/fpm.d\/\\*\\.conf|;include\s*=\s*\/etc\/php5\/fpm.d\/\\*\\.conf|g"
/etc/php5/php-fpm.conf \  
&& sed -i "s|group\s*=\s*nobody|group = ${PHP_FPM_GROUP}|g" /etc/php5/php-
fpm.conf \  
&& sed -i "s|;log_level\s*=\s*notice|log_level = notice|g" /etc/php5/php-
fpm.conf #uncommenting line  
  
# PHP Update Config  
# https://github.com/electerious/Lychee/blob/master/docs/Installation.md  
RUN sed -i "s|;*max_execution_time =.*|max_execution_time =
${PHP_MAX_EXEC_TIME}|i" /etc/php5/php.ini \  
&& sed -i "s|;*post_max_size =.*|post_max_size = ${PHP_POST_MAX_SIZE}|i"
/etc/php5/php.ini \  
&& sed -i "s|;*upload_max_filesize =.*|upload_max_filesize =
${PHP_UPLOAD_MAX_SIZE}|i" /etc/php5/php.ini \  
&& sed -i "s|;*max_file_uploads =.*|max_file_uploads =
${PHP_UPLOAD_MAX_FILESIZE}|i" /etc/php5/php.ini \  
&& sed -i "s|;*memory_limit =.*|memory_limit = ${PHP_MEMORY_LIMIT}|i"
/etc/php5/php.ini  
  
# Create Webserver Directory  
RUN mkdir /www  
  
# Add User and Fix permissions  
RUN adduser -D -g 'www' www \  
&& chown -R www:www /var/lib/nginx \  
&& chown -R www:www /www  
  
WORKDIR /www  
  
# Clone Repository Update permissions  
RUN git clone https://github.com/electerious/Lychee.git /www \  
&& chown -R www:www /www \  
&& chmod -R 770 /www \  
&& chmod -R 777 /var/tmp/nginx \  
&& mkdir /var/tmp/nginx/client_body \  
&& chmod -R 777 /var/tmp/nginx/client_body \  
&& chmod -R 777 /www/uploads/ \  
&& chmod -R 777 /www/data/  
  
# Expose Ports  
EXPOSE 9000  
EXPOSE 80  
  
VOLUME /www/uploads  
VOLUME /www/data  
  
WORKDIR /  
  
CMD ["/usr/bin/supervisord", "-n", "-c", "/supervisord.conf"]  

