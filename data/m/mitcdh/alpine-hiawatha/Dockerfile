FROM alpine:edge  
MAINTAINER Mitchell Hewes <me@mitcdh.com>  
  
RUN apk add --update \  
musl \  
libxslt \  
zlib \  
libxml2 \  
mbedtls && \  
apk add hiawatha --update-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted && \  
rm -rf /var/cache/apk/*  
  
# Add user and group  
RUN addgroup -S www-data && \  
adduser -S -G www-data -g "Web Server" -h "/www" web-srv  
  
# Add configuration  
ADD files/hiawatha.conf /etc/hiawatha/hiawatha.conf  
ADD files/run.sh /scripts/run.sh  
RUN mkdir /scripts/pre-run/  
RUN chmod -R 700 /scripts/  
RUN mkdir /etc/hiawatha/conf.d  
RUN chown web-srv:www-data /etc/hiawatha/conf.d  
  
EXPOSE 80  
CMD ["/scripts/run.sh"]  

