FROM wordpress:php7.1  
LABEL maintainer="Seti <seti@setadesign.net>"  
  
RUN apt update && apt install zlib1g-dev && docker-php-ext-install zip \  
apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false;
\  
rm -rf /var/lib/apt/lists/*

