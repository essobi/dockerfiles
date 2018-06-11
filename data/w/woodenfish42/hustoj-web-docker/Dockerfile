FROM alpine  
LABEL maintainer="muzea <mr.muzea@gmail.com>"  
  
ENV TIMEZONE Asia/Shanghai  
ENV PHP_MEMORY_LIMIT 512M  
ENV MAX_UPLOAD 50M  
ENV PHP_MAX_FILE_UPLOAD 200  
ENV PHP_MAX_POST 100M  
  
RUN set -ex \  
&& apk update \  
&& apk upgrade \  
&& apk add --no-cache \  
git \  
tar \  
nginx \  
php5-mcrypt \  
php5-openssl \  
php5-gmp \  
php5-json \  
php5-dom \  
php5-pdo \  
php5-zip \  
php5-mysql \  
php5-xml \  
php5-gd \  
php5-pdo_mysql \  
php5-bz2 \  
php5-iconv \  
php5-curl \  
php5-ctype \  
php5-fpm \  
&& sed -i "s|;*daemonize\s*=\s*yes|daemonize = no|g" /etc/php5/php-fpm.conf \  
&& sed -i "s|;*listen\s*=\s*127.0.0.1:9000|listen = 9000|g" /etc/php5/php-
fpm.conf \  
&& sed -i "s|;*listen\s*=\s*/||g" /etc/php5/php-fpm.conf \  
&& sed -i "s|;*date.timezone =.*|date.timezone = ${TIMEZONE}|i"
/etc/php5/php.ini \  
&& sed -i "s|;*memory_limit =.*|memory_limit = ${PHP_MEMORY_LIMIT}|i"
/etc/php5/php.ini \  
&& sed -i "s|;*upload_max_filesize =.*|upload_max_filesize = ${MAX_UPLOAD}|i"
/etc/php5/php.ini \  
&& sed -i "s|;*max_file_uploads =.*|max_file_uploads =
${PHP_MAX_FILE_UPLOAD}|i" /etc/php5/php.ini \  
&& sed -i "s|;*post_max_size =.*|post_max_size = ${PHP_MAX_POST}|i"
/etc/php5/php.ini \  
&& sed -i "s|;*cgi.fix_pathinfo=.*|cgi.fix_pathinfo= 0|i" /etc/php5/php.ini \  
# Cleaning up  
&& cd / && git clone https://github.com/zhblue/hustoj.git \  
&& mv /hustoj/trunk/web /www \  
&& rm -rf /hustoj \  
&& rm -rf /var/cache/apk/* \  
&& mkdir /run/nginx  
  
COPY nginx/default.conf /etc/nginx/conf.d/default.conf  
WORKDIR /www  
EXPOSE 80  
  
CMD /usr/sbin/nginx && /usr/bin/php-fpm5  

