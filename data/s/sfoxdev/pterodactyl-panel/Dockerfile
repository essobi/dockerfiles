FROM alpine:3.6  
MAINTAINER SFoxDev <admin@sfoxdev.com>  
  
ENV PANEL_VERSION=v0.6.4 \  
STARTUP_TIMEOUT=5 \  
LC_ALL=C.UTF-8 \  
LANG=en_US.UTF-8 \  
LANGUAGE=en_US.UTF-8  
WORKDIR /var/www/html  
  
RUN apk update && apk add \  
curl gettext nginx supervisor bash mc \  
php7 php7 php7-bcmath php7-common php7-dom php7-fpm php7-gd php7-memcached
php7-mbstring php7-openssl \  
php7-pdo php7-phar php7-json php7-pdo_mysql php7-session php7-tokenizer
php7-ctype php7-zlib php7-zip \  
&& mkdir -p /var/www/html /run/nginx \  
&& curl -Lo "${PANEL_VERSION}.tar.gz"
https://github.com/Pterodactyl/Panel/archive/${PANEL_VERSION}.tar.gz \  
&& tar --strip-components=1 -xzvf ${PANEL_VERSION}.tar.gz \  
&& rm "${PANEL_VERSION}.tar.gz" \  
&& chmod -R 755 storage/* bootstrap/cache \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& composer install --ansi --no-dev \  
&& mv ./storage storage.tmpl \  
&& chown nginx:nginx * -R \  
&& rm -rf /var/cache/apk/* /tmp/*  
  
COPY ./manifest /  
  
VOLUME [ "/data" ]  
  
EXPOSE 80 443  
ENTRYPOINT [ "/bin/ash", "/entrypoint.sh" ]  
  
CMD [ "p:start" ]  

