FROM alpine:edge  
MAINTAINER Christoph Wiechert <wio@psitrax.de>  
  
RUN apk update \  
&& apk add bash nginx php-fpm php-json ca-certificates php-openssl \  
owncloud-mysql owncloud-videoviewer owncloud-tasks owncloud-texteditor
owncloud-calendar owncloud-contacts  
  
# fix php-fpm "Error relocating /usr/bin/php-fpm: __flt_rounds: symbol not
found" bug  
RUN apk add -u musl  
RUN rm -rf /var/cache/apk/*  
  
ADD files/nginx.conf /etc/nginx/  
ADD files/php-fpm.conf /etc/php/  
ADD files/config.php /tmp/  
ADD files/autoconfig.php /tmp/  
ADD files/run.sh /  
RUN chmod +x /run.sh  
  
EXPOSE 80  
VOLUME ["/DATA"]  
  
CMD ["/run.sh"]  

