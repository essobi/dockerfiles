FROM php:7  
RUN apt-get update -y && apt-get install -y openssl zip unzip git  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN docker-php-ext-install mysqli pdo_mysql pdo mbstring  
  
WORKDIR /app  
COPY . /app  
COPY .env.example .env  
  
RUN composer install && php artisan key:generate  
  
ENV DB_CONNECTION=mysql  
ENV DB_HOST=mysql  
ENV DB_PORT=3306  
ENV DB_DATABASE=siwecos_business_layer  
ENV DB_USERNAME=siwecos  
ENV DB_PASSWORD=n0ucav3z  
ENV CORE_URL=siwecoscoreapi:8666  
ENV CORE_MASTER_TOKEN=KFHN1NwMkiLtlZ9UXZZrbAoT  
#RUN php artisan migrate  
#RUN php artisan create:mastertoken  
CMD php artisan serve --host=0.0.0.0 --port=8667  
EXPOSE 8667  

