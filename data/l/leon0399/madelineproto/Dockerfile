FROM php:alpine  
LABEL maintainer="Leonid Meleshin <leon.03.99@gmail.com>"  
  
RUN docker-php-ext-install sockets  
RUN docker-php-ext-install pcntl  
  
WORKDIR /app  
COPY "entrypoint.php" "./"  
ADD https://phar.madelineproto.xyz/madeline.phar?v=new madeline.phar  
  
ENTRYPOINT [ "php", "./entrypoint.php", "80" ]  
CMD [ "strong" ]  
  
EXPOSE 80  

