FROM node:alpine  
MAINTAINER Fanel Dabija <faneldabija2008@gmail.com>  
  
ENV PHP_OPCACHE_ENABLE 0  
ENV APP_DIR /var/www  
ENV APP_ENV dev  
  
RUN apk --no-cache add nginx php7 php7-fpm php7-json php7-ctype php7-mbstring
php7-curl php7-opcache && \  
rm -rf /var/cache/apk/* /tmp/*  
  
COPY ./etc /etc  
COPY ./usr /usr  
  
RUN chmod +x /usr/bin/*  
  
RUN npm install nodemon -g  
  
VOLUME $APP_DIR  
WORKDIR $APP_DIR  
  
EXPOSE 3000  
CMD ["entrypoint"]  

