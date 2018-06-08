FROM alpine:3.3  
MAINTAINER daxingplay <daxingplay@gmail.com>  
  
ENV VERSION=3.3  
RUN apk update \  
&& apk add bash curl tar gzip nginx ca-certificates \  
php-fpm php-json php-zlib php-xml php-pdo php-phar php-openssl \  
php-pdo_mysql php-mysqli \  
php-gd php-iconv php-mcrypt \  
php-mysql php-curl php-opcache php-ctype php-apcu \  
php-intl php-bcmath php-dom php-xmlreader mysql-client && apk add -u musl  
  
# download SolusVMController  
RUN curl -sSL
https://github.com/seikan/SolusVMController/archive/${VERSION}.tar.gz | tar
xfz - -C / && \  
mv SolusVMController-${VERSION} srv && \  
chown -R nginx:www-data /srv/ && \  
rm -f /srv/configuration.php.default && \  
rm -f /srv/setup.php  
  
# cleanup  
RUN rm -rf /var/cache/apk/*  
  
ENV TERM="xterm" \  
DB_HOST="172.17.0.1" \  
DB_NAME="" \  
DB_USER=""\  
DB_PASS=""  
RUN sed -i 's/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g' /etc/php/php.ini && \  
sed -i 's/nginx:x:100:101:Linux
User,,,:\/var\/www\/localhost\/htdocs:\/sbin\/nologin/nginx:x:100:101:Linux
User,,,:\/var\/www\/localhost\/htdocs:\/bin\/bash/g' /etc/passwd && \  
sed -i 's/nginx:x:100:101:Linux
User,,,:\/var\/www\/localhost\/htdocs:\/sbin\/nologin/nginx:x:100:101:Linux
User,,,:\/var\/www\/localhost\/htdocs:\/bin\/bash/g' /etc/passwd-  
  
ADD src /  
RUN chmod +x /run.sh  
  
EXPOSE 80  
VOLUME ["/DATA"]  
  
CMD ["/run.sh"]  

