FROM alpine:edge  
MAINTAINER Jeroen Geusebroek <me@jeroengeusebroek.nl>  
  
ARG VERSION=0.22  
ENV GID=991 UID=991  
RUN echo -e "@edge http://nl.alpinelinux.org/alpine/edge/main\n@testing
http://nl.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories \  
&& apk -U add \  
curl \  
nginx \  
php7-fpm@testing \  
php7-gd@testing \  
php7-mcrypt@testing \  
php7-json@testing \  
php7-zlib@testing \  
supervisor \  
tini \  
ca-certificates \  
tar \  
  
&& mkdir zerobin && cd zerobin \  
&& curl -L -o zerobin.tar.gz
https://github.com/elrido/ZeroBin/archive/$VERSION.tar.gz \  
&& tar xvzf zerobin.tar.gz --strip 1 \  
&& rm zerobin.tar.gz \  
  
&& mv cfg/conf.ini.sample /zerobin \  
&& apk del tar ca-certificates \  
&& rm -f /var/cache/apk/*  
  
COPY files/nginx.conf /etc/nginx/nginx.conf  
COPY files/php-fpm.conf /etc/php7/php-fpm.conf  
COPY files/supervisord.conf /usr/local/etc/supervisord.conf  
COPY entrypoint.sh /  
  
RUN chmod +x /entrypoint.sh  
  
VOLUME [ "/zerobin/data", "/zerobin/cfg" ]  
  
EXPOSE 80  
LABEL description "A minimalist, opensource online pastebin where the server
has zero knowledge of pasted data" \  
zerobin "elrido's ZeroBin v$VERSION"  
CMD ["tini","--","/entrypoint.sh"]  

