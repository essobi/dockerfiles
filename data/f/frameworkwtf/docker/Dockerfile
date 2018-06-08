FROM alpine:latest  
  
ENV PHP_OPCACHE_ENABLE 0  
ENV BLACKFIRE_HOST blackfire  
ENV BLACKFIRE_LOG_LEVEL 1  
ENV APP_DIR /var/www  
ENV APP_ENV dev  
ENV APP_RELEASE local  
ENV APP_HOST localhost  
ENV APP_SECRET qwerty  
  
ADD https://blackfire.io/api/v1/releases/probe/php/alpine/amd64/71
/tmp/blackfire-probe.tar.gz  
RUN apk --no-cache add nginx php7 php7-fpm php7-json php7-ctype php7-mbstring
php7-curl php7-opcache php7-session tar && \  
tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp && \  
mv /tmp/blackfire-*.so /usr/lib/php7/modules/blackfire.so && \  
apk --no-cache del tar && rm -rf /var/cache/apk/* /tmp/*  
  
COPY ./etc /etc  
COPY ./usr /usr  
  
RUN chmod +x /usr/bin/*  
  
VOLUME $APP_DIR  
WORKDIR $APP_DIR  
  
EXPOSE 8080  
CMD ["entrypoint"]  

