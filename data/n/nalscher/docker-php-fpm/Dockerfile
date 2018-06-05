FROM php:5.6-fpm-alpine  
  
ENV PUID 1000  
ENV GUID 1000  
  
ENV APP_ROOT /var/www/html  
ENV NR_VERSION newrelic-php5-7.7.0.203-linux-musl  
ENV NR_INSTALL_SILENT true  
ENV APP_DATETIME UTC  
ENV APP_POST_SIZE 64M  
ENV APP_MEMORY_LIMIT 256M  
ENV APP_MAX_EXECUTION_TIME 120  
ENV APP_MAX_CHILDREN 20  
ENV APP_PROCESS_IDLE_TIMEOUT 10s  
  
ENV APP_ENVIRONMENT production  
ENV APP_DEPLOY_ENV production  
  
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/community/ >>
/etc/apk/repositories  
  
RUN apk update && \  
apk add \--no-cache shadow icu-dev g++ autoconf openssl-dev \  
make pcre pcre-dev bash msttcorefonts-installer \  
gnumeric libssh2-dev openssh-client bzip2-dev ffmpeg && \  
docker-php-ext-configure intl && \  
docker-php-ext-configure opcache && \  
docker-php-ext-configure zip && \  
docker-php-ext-configure bz2 && \  
docker-php-ext-configure iconv && \  
docker-php-ext-install intl opcache zip bz2 iconv && \  
update-ms-fonts && \  
fc-cache -f && \  
pecl install mongodb-1.2.11 && \  
printf "\n" | pecl install apcu-4.0.11 && \  
printf "\n" | pecl install ssh2  
  
RUN echo "extension=mongodb.so" > /usr/local/etc/php/conf.d/zz-pc-mongodb.ini
&& \  
echo "extension=apcu.so" > /usr/local/etc/php/conf.d/zz-pc-apcu.ini && \  
echo "extension=ssh2.so" > /usr/local/etc/php/conf.d/zz-pc-ssh2.ini && \  
  
printf "[Date]\ndate.timezone = \"${APP_DATETIME}\"" >
/usr/local/etc/php/conf.d/zz-pc-timezone.ini && \  
  
echo "opcache.fast_shutdown = 0" > /usr/local/etc/php/conf.d/zz-pc-opcache.ini
&& \  
echo "opcache.enable_cli = 0" >> /usr/local/etc/php/conf.d/zz-pc-opcache.ini
&& \  
  
echo "upload_max_filesize = ${APP_POST_SIZE}" > /usr/local/etc/php/conf.d/zz-
pc-limit.ini && \  
echo "post_max_size = ${APP_POST_SIZE}" >> /usr/local/etc/php/conf.d/zz-pc-
limit.ini && \  
echo "memory_limit = ${APP_MEMORY_LIMIT}" >> /usr/local/etc/php/conf.d/zz-pc-
limit.ini && \  
echo "max_execution_time = ${APP_MAX_EXECUTION_TIME}" >>
/usr/local/etc/php/conf.d/zz-pc-limit.ini && \  
  
echo "display_errors = Off" > /usr/local/etc/php/conf.d/zz-pc-errors.ini && \  
echo "log_errors = on" >> /usr/local/etc/php/conf.d/zz-pc-errors.ini && \  
echo "error_log = /var/log/php/error.log" >> /usr/local/etc/php/conf.d/zz-pc-
errors.ini && \  
echo "error_reporting = E_ALL & ~E_DEPRECATED & ~E_STRICT" >>
/usr/local/etc/php/conf.d/zz-pc-errors.ini  
  
RUN echo "[www]" > /usr/local/etc/php-fpm.d/zz-www.conf && \  
echo "pm = ondemand" > /usr/local/etc/php-fpm.d/zz-www.conf && \  
echo "pm.max_children = ${APP_MAX_CHILDREN}" >> /usr/local/etc/php-fpm.d/zz-
www.conf && \  
echo "pm.process_idle_timeout = ${APP_PROCESS_IDLE_TIMEOUT}" >>
/usr/local/etc/php-fpm.d/zz-www.conf  
  
RUN mkdir /var/log/php && cd /var/log/php && ln -s /dev/stderr error.log  
  
# @see : https://github.com/docker-library/php/issues/240 or
https://gist.github.com/guillemcanal/be3db96d3caa315b4e2b8259cab7d07e  
RUN apk add \--no-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/testing gnu-libiconv  
ENV LD_PRELOAD /usr/lib/preloadable_libiconv.so php  
ENV LD_PRELOAD /usr/lib/preloadable_libiconv.so php-fpm  
  
RUN cd && \  
wget http://download.newrelic.com/php_agent/release/${NR_VERSION}.tar.gz && \  
gzip -dc ${NR_VERSION}.tar.gz | tar xf - && \  
cd ${NR_VERSION} && \  
./newrelic-install install  
  
ADD start.sh /start.sh  
RUN chmod 755 /start.sh  
  
CMD ["/start.sh"]  

