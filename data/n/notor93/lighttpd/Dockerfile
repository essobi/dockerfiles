FROM alpine:3.6  
# environments  
ENV PHP_CONTAINER_HOST 'php'  
RUN apk add --update --no-cache lighttpd  
  
# 82 is the standard uid/gid for "www-data" in Alpine and 1000 is the dev user  
RUN set -x \  
&& addgroup -g 1000 -S dev \  
&& adduser -u 1000 -D -S -G dev dev \  
&& adduser -u 82 -D -S -G www-data www-data \  
&& addgroup www-data dev  
  
COPY rootfs/ /etc/lighttpd/  
COPY entrypoint.sh /usr/bin/entrypoint.sh  
  
RUN chmod u+x /usr/bin/entrypoint.sh  
  
RUN mkdir -p /var/www /var/lib/lighttpd/cache/compress /var/log/lighttpd \  
&& chown -R www-data:www-data /var/lib/lighttpd/cache/compress
/var/log/lighttpd  
  
WORKDIR /var/www  
  
EXPOSE 80  
ENTRYPOINT ["/usr/bin/entrypoint.sh"]  
  
CMD ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]  

