FROM alpine:edge  
MAINTAINER Pooya Parsa <pooya@pi0.ir>  
  
RUN apk update \  
&& apk add bash less vim nginx ca-certificates \  
php-fpm php-json php-zlib php-xml php-pdo php-phar php-openssl \  
php-pdo_mysql php-mysqli \  
php-gd php-iconv php-mcrypt \  
php-mysql php-curl php-opcache php-ctype php-apcu \  
php-intl php-bcmath php-dom php-xmlreader mysql-client && apk add -u musl  
  
RUN rm -rf /var/cache/apk/*  
  
RUN sed -i 's/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g' /etc/php/php.ini  
  
ENV TERM="xterm"  
ADD docker_init /  
ADD nginx.conf /etc/nginx/  
ADD php-fpm.conf /etc/php/  
  
EXPOSE 80  
VOLUME ["/data"]  
CMD ["/docker_init"]

