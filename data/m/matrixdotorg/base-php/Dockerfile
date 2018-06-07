FROM docker.io/matrixdotorg/base-caddy  
ENV APPDIR=/phpapp  
RUN apk add --no-cache \  
php7-fpm \  
php7  
ADD root /  
EXPOSE 8888  

