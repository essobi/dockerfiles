FROM wordpress:latest  
MAINTAINER Nasajon<devops@nasason.com.br>  
  
RUN apt-get update && apt-get install -y \  
libmcrypt-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install -j$(nproc) mcrypt

