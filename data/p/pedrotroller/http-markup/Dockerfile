FROM php:7.1.1-apache  
  
RUN apt-get update && \  
apt-get install ruby ruby-dev git -y && \  
gem install github-markup redcarpet RedCloth org-ruby creole asciidoctor && \  
rm -rf /var/lib/apt/lists/*  
  
COPY composer.* /var/www/html/  
  
RUN curl -sS https://getcomposer.org/installer | php && \  
php composer.phar install --prefer-dist --optimize-autoloader && \  
rm composer.phar  
  
COPY . /var/www/html  
  

