FROM php:7.1-fpm-alpine  
  
VOLUME ["/var/app"]  
WORKDIR /opt/app  
  
COPY setup-phpext.sh /  
RUN sh /setup-phpext.sh && rm /setup-*.sh  
COPY fpm-production.ini /usr/local/etc/php/conf.d/kendu-fpm-production.ini  
  
ENV LOG_STREAM="/tmp/stdout"  
RUN mkfifo $LOG_STREAM && chmod 777 $LOG_STREAM  
CMD ["sh", "-o", "pipefail", "-c", "php-fpm -D | tail -f $LOG_STREAM"]

