FROM codeception/codeception  
  
RUN apt-get update && \  
rm -rf /var/lib/apt/lists/*  
  
RUN docker-php-ext-install \  
pdo_mysql  
  
RUN mkdir -p /var/www/html  
WORKDIR /var/www/html  

