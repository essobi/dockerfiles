FROM musclerumble/apache-php-apcu  
  
RUN apt-get update && \  
apt-get install -y \  
libgmp-dev && \  
rm -rf /var/lib/apt/lists/* &&\  
ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/local/include/  
  
RUN docker-php-ext-install gmp  
RUN docker-php-ext-enable gmp  
  
COPY src/ /var/www/html/  

