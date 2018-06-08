FROM tsterk/tsterk-base-alpine  
MAINTAINER Tim Sterk <tim.sterk@gmail.com>  
  
RUN apk add --no-cache php7-fpm && \  
ln -sfn /dev/stderr /var/log/php7/error.log  
  
COPY ./www.conf /etc/php7/php-fpm.d/www.conf  
  
EXPOSE 9000  
CMD ["php-fpm7", "-F"]

