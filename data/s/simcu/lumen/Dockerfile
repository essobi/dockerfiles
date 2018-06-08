FROM alpine:3.5  
COPY files /home/install  
RUN apk add \--update php7 php7-xml php7-pdo php7-openssl php7-fpm php7-zip
php7-mbstring \  
php7-sockets php7-gettext php7-iconv php7-pdo_pgsql php7-zlib php7-soap \  
php7-bz2 php7-json php7-phar php7-ctype php7-gd php7-bcmath php7-curl nginx &&
\  
sh /home/install/config.sh && \  
rm -rf /home/install && \  
rm -rf /var/cache/apk/*  
WORKDIR /home  
CMD "/run.sh"

