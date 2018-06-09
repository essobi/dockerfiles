FROM wordpress:php7.0-fpm-alpine  
  
ENV TIMEZONE Europe/Moscow  
  
RUN apk add --no-cache -U tzdata && \  
cp /usr/share/zoneinfo/Europe/Moscow /etc/localtime && \  
echo "Europe/Moscow" > /etc/timezone && \  
apk del tzdata  

