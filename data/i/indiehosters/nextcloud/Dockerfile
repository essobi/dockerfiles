FROM nextcloud:13-fpm  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libc-client-dev \  
libkrb5-dev \  
libmagickwand-dev \  
&& docker-php-ext-configure imap --with-kerberos --with-imap-ssl \  
&& docker-php-ext-install imap \  
&& pecl install imagick \  
&& docker-php-ext-enable imagick \  
&& rm -rf /var/lib/apt/lists/*  

