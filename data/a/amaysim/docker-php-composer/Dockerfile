FROM composer:1.4.2  
RUN apk --no-cache add --update \  
mysql-client \  
libmcrypt \  
libmcrypt-dev \  
openssl \  
zlib-dev \  
libxml2-dev  
  
RUN docker-php-ext-install mcrypt pdo pdo_mysql zip mbstring soap tokenizer
bcmath  
RUN touch /etc/ssh/ssh_config && \  
echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config  

