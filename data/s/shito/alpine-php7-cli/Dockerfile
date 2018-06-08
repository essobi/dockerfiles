FROM alpine:edge  
MAINTAINER Sebastian Knoth <sk@bytepark.de>  
  
# Add PHP 7  
RUN apk upgrade -U && \  
apk --update --repository=http://dl-4.alpinelinux.org/alpine/edge/testing add
\  
php7  
  
# Small fixes  
RUN ln -s /etc/php7 /etc/php && \  
ln -s /usr/bin/php7 /usr/bin/php && \  
ln -s /usr/lib/php7 /usr/lib/php && \  
rm -fr /var/cache/apk/*  
  
COPY rootfs/ /  
  
ENTRYPOINT ["php"]  
CMD ["--help"]

