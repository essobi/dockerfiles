FROM alpine:3.5  
MAINTAINER Jamie Curnow <jc@jc21.com>  
LABEL maintainer="Jamie Curnow <jc@jc21.com>"  
  
ENV S6_FIX_ATTRS_HIDDEN=1  
RUN echo "fs.file-max = 65535" > /etc/sysctl.conf  
  
# root filesystem  
COPY rootfs /  
  
# s6 overlay  
RUN apk add --no-cache curl \  
&& curl -L -s https://github.com/just-
containers/s6-overlay/releases/download/v1.19.1.1/s6-overlay-amd64.tar.gz \  
| tar xzf - -C / \  
&& apk del --no-cache curl  
  
# Install  
RUN apk update && apk upgrade \  
&& apk add \  
bash jq curl vim ca-certificates s6 ssmtp \  
php7 php7-phar php7-curl php7-fpm php7-json php7-zlib php7-xml php7-xmlreader
php7-dom php7-ctype \  
php7-opcache php7-zip php7-iconv php7-pdo php7-pdo_mysql php7-pdo_sqlite
php7-pdo_pgsql \  
php7-mbstring php7-session php7-gd php7-mcrypt php7-openssl php7-sockets
php7-posix \  
php7-ldap php7-mysqli php7-soap php7-apcu php7-gmp php7-pgsql \  
php7-ftp php7-gettext nginx nginx-mod-http-lua \  
&& ln -s /usr/bin/php7 /usr/bin/php  
  
# fix php7-fpm "Error relocating /usr/bin/php7-fpm: __flt_rounds: symbol not
found" bug  
RUN apk add -u musl && rm -rf /var/cache/apk/*  
  
# Shell Fix  
RUN echo "/bin/bash" >> /etc/shells  
RUN sed -i -- 's/bin\/ash/bin\/bash/g' /etc/passwd  
ADD env/.bashrc /root/  
  
# Nginx  
RUN rm -rf /var/www/* && mkdir -p /etc/nginx/conf.d /var/app /run/nginx
/tmp/nginx/fastcgi_temp /tmp/nginx/body /var/run/php7-fpm  
  
ENTRYPOINT [ "/init" ]  

