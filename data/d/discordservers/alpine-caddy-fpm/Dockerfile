FROM php:rc-fpm-alpine  
MAINTAINER discordservers <admin@discordservers.com>  
  
ENV BUILD_PACKAGES="pcre-dev make gcc g++ openssh-client tar python py-pip
autoconf" \  
ESSENTIAL_PACKAGES="git zip curl zlib supervisor pcre linux-headers go
postgresql-dev" \  
GOPATH="/root/go"  
RUN apk add --update --no-cache --progress $ESSENTIAL_PACKAGES $BUILD_PACKAGES
\  
&& apk add --virtual devs curl \  
&& pip install supervisor-stdout \  
&& docker-php-ext-install pdo pdo_mysql pdo_pgsql sockets \  
&& pecl install redis apcu swoole \  
&& mkdir -p $GOPATH/src \  
&& cd $GOPATH/src \  
&& go get -u github.com/mholt/caddy \  
&& go get -u github.com/caddyserver/builds \  
&& cd $GOPATH/src/github.com/mholt/caddy/caddy \  
&& git checkout tags/v0.10.10 \  
&& go run build.go -goos=linux -goarch=amd64 \  
&& mv caddy /usr/local/sbin/caddy \  
&& apk del $BUILD_PACKAGES \  
&& curl --silent --show-error https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& chmod +x /usr/local/bin/composer \  
&& composer global require hirak/prestissimo  
  
COPY ./manifest /  
  
EXPOSE 80  
CMD /usr/bin/supervisord -n -c /etc/supervisord.conf

