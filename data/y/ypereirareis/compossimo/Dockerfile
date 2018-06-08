ARG COMPOSER_VERSION=1.6.4  
FROM composer:$COMPOSER_VERSION  
MAINTAINER yannick Pereira-Reis <yannick.pereira-reis@sfam.eu>  
  
ARG USER_ID=1000  
ENV COMPOSER_ALLOW_SUPERUSER 0  
ENV WORKDIR /app  
  
RUN set -x \  
&& addgroup -g $USER_ID -S composer \  
&& adduser -u $USER_ID -D -S -G composer composer  
  
USER composer  
  
RUN composer global require hirak/prestissimo  
  

