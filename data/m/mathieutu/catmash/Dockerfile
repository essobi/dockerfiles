FROM php:latest  
MAINTAINER Mathieu TUDISCO <dev@mathieutu.ovh>  
RUN apt-get update -y && apt-get install -y openssl zip unzip git  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash  
RUN apt-get install -y nodejs  
  
RUN curl -o- -L https://yarnpkg.com/install.sh | bash  
ENV PATH "$HOME/.yarn/bin:$PATH"  
RUN docker-php-ext-install pdo pdo_mysql mbstring  
  
WORKDIR /app  
COPY . /app  
  
RUN composer install --no-dev --no-interaction  
  
ADD .env.prod /app/.env  
RUN php artisan key:generate  
  
RUN $HOME/.yarn/bin/yarn install --force  
RUN $HOME/.yarn/bin/yarn production  
RUN rm -Rf nodes_module  
  
CMD php artisan migrate --force && php artisan serve --host=0.0.0.0 --port=80  
  
EXPOSE 80  

