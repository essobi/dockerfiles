FROM alpine:3.2  
MAINTAINER Jean Bordat <bordat.jean@gmail.com>  
  
RUN apk update \  
&& apk add --update bash nginx ca-certificates curl \  
php-fpm php-json php-zlib php-xml php-pdo php-phar php-openssl \  
php-pdo_mysql php-mysqli php-ctype php-dom \  
php-gd php-iconv php-mcrypt \  
git  
  
# Coposer installation  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
# fix php-fpm "Error relocating /usr/bin/php-fpm: __flt_rounds: symbol not
found" bug  
RUN apk add -u musl  
RUN rm -rf /var/cache/apk/*  
  
ADD files/nginx.conf /etc/nginx/  
ADD files/php-fpm.conf /etc/php/  
ADD files/run.sh /  
RUN chmod +x /run.sh  
ADD files/run_app_preparation.sh /  
RUN chmod +x /run_app_preparation.sh  
  
# APP_TYPE can be: Symfony2 | ...  
ENV APP_TYPE Symfony2  
  
# ENV can be : Development | Staging | Production  
ENV ENV Development  
  
# DB_LINKED can be true | false  
# default False  
# If true, script will update database structure  
ENV DB_LINKED false  
  
# CI_VERSION can be everything.  
ENV CI_VERSION to_be_defined  
  
  
EXPOSE 80  
VOLUME ["/DATA"]  
  
CMD ["/run.sh"]

