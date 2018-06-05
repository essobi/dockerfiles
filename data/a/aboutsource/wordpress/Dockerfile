FROM aboutsource/php-fpm:5.6  
MAINTAINER support@aboutsource.net  
  
RUN curl -Ls -o /usr/local/bin/wp https://github.com/wp-cli/wp-
cli/releases/download/v0.23.1/wp-cli-0.23.1.phar && \  
chmod +x /usr/local/bin/wp  
  
RUN apt-get update && apt-get install -y --no-install-recommends less && rm
-rf /var/lib/apt/lists/*  
  
RUN curl -Ls -o /usr/local/bin/composer
https://getcomposer.org/download/1.1.3/composer.phar && \  
chmod +x /usr/local/bin/composer  
  
COPY wordpress-debug-tools /usr/local/src/wordpress-debug-tools  

