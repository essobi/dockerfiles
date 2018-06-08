FROM k0st/alpine-apache-php  
  
ENV WORKDIR /app  
  
RUN apk --update add git zip unzip php-dom php-ctype bash  
  
RUN git clone https://github.com/picocms/Pico.git $WORKDIR  
  
WORKDIR $WORKDIR  
  
RUN composer install --no-dev --no-interaction  
  
EXPOSE 80  

