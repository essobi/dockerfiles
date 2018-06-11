FROM wordpress:4.9  
  
RUN apt-get update && apt-get install -y zlib1g-dev && rm -rf
/var/lib/apt/lists/* && docker-php-ext-install zip  

