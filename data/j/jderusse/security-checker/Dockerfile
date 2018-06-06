FROM alpine:edge  
RUN echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
  
# PHP  
RUN apk add --no-cache \  
php7 \  
&& ln -s /usr/bin/php7 /usr/bin/php  
  
# Install security checker  
RUN apk add --no-cache \  
curl  
  
RUN curl -s http://get.sensiolabs.org/security-checker.phar >
/usr/local/bin/security-checker \  
&& chmod +x /usr/local/bin/security-checker  
  
# Performances matter  
RUN apk add --no-cache \  
php7-opcache \  
php7-apcu@testing  
  
# Symfony requirements  
RUN apk add --no-cache \  
php7-phar \  
php7-mbstring \  
php7-openssl \  
php7-json \  
  
php7-posix  
  
  
RUN echo $'\n\  
opcache.enable_cli=1 \n\  
opcache.file_cache=/tmp/opcache \n\  
opcache.file_update_protection=0 \n'\  
>> /etc/php7/conf.d/security-checker.ini \  
  
&& mkdir -p /tmp/opcache  
  
# Warmup  
RUN security-checker \  
&& security-checker security:check || true  
  
VOLUME ["/src"]  
WORKDIR /src  
  
ENTRYPOINT ["security-checker"]  
CMD ["security:check"]  

