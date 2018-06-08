FROM alpine:edge  
MAINTAINER Yurii Fisakov <fisakov.root@gmail.com>  
ENV TIMEZONE Europe/Kiev  
ENV PHP_MEMORY_LIMIT 512M  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk update && \  
apk upgrade && \  
apk add --update tzdata && \  
cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \  
echo "${TIMEZONE}" > /etc/timezone && \  
apk add --update \  
sed \  
php7 \  
php-xmlwriter \  
php7-curl \  
php7-json  
  
RUN mkdir /www /export && \  
apk del tzdata && \  
rm -rf /var/cache/apk/*  
  
COPY source/* /www/  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod 0755 /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  

