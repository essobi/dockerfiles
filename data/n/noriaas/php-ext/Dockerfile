################################################################################  
# Base image  
################################################################################  
  
FROM noriaas/php:stable  
  
ENV DEFAULT_APP_USER=noria \  
DEFAULT_APP_GROUP=noria \  
DEFAULT_APP_UID=1000 \  
DEFAULT_APP_GID=1000 \  
DEFAULT_FPM_LISTEN='/var/run/noria/portal7.1.sock' \  
DEFAULT_FPM_MAXCHILDREN=12  
  
################################################################################  
# Build instructions  
################################################################################  
  
# Add configuration files  
COPY conf/portal7.1.sock.conf /tmp/portal7.1.sock.conf.default  
COPY conf/php.ini /usr/local/etc/php/  
  
RUN apk add --no-cache --virtual .run-deps gosu su-exec && \  
set -e \  
&& cd /usr/local/etc \  
&& \  
if ! [ -d "php-fpm.d" ]; then \  
mkdir php-fpm.d; \  
cp /tmp/portal7.1.sock.conf.default php-fpm.d/portal.conf; \  
else \  
# PHP 5.x doesn't use "include=" by default, so we'll create our own simple
config that mimics PHP 7\+ for consistency  
cp -f /tmp/portal7.1.sock.conf.default php-fpm.d/portal.conf.default; \  
  
if [ -f php-fpm.d/www.conf ] ; then \  
rm -f php-fpm.d/www.conf; \  
echo $'\n\  
[global] \n \  
error_log = /proc/self/fd/2 \n' > php-fpm.d/docker.conf; \  
echo $'\n\  
[global] \n\  
daemonize = no \n' > php-fpm.d/zz-docker.conf; \  
fi; \  
{ \  
echo '[global]'; \  
echo 'include=etc/php-fpm.d/*.conf'; \  
} | tee php-fpm.conf; \  
fi  
  
  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
#STOPSIGNAL SIGTERM  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["php-fpm"]

