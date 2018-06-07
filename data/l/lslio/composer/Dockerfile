FROM composer:latest  
  
RUN composer global require hirak/prestissimo \  
--prefer-dist \  
--prefer-stable \  
--no-progress \  
--no-scripts \  
--no-suggest \  
--no-interaction \  
--ansi  
  
# Install and Autoloader generation is split  
# Allows install step to occur earlier than your code copy step  
RUN echo 'composer install \  
--ignore-platform-reqs \  
--no-dev \  
--no-autoloader \  
--no-scripts \  
--no-progress \  
--no-suggest \  
--no-interaction \  
--ansi "$@"' > /usr/bin/composer-install && \  
chmod +x /usr/bin/composer-install  
  
RUN echo 'composer dump-autoload \  
--optimize \  
--classmap-authoritative \  
--apcu \  
--no-dev \  
--ansi "$@"' > /usr/bin/composer-dump-autoload && \  
chmod +x /usr/bin/composer-dump-autoload  
  
# Quickest, cleanest way to require single composer applications  
RUN echo 'composer require \  
--ignore-platform-reqs \  
--no-scripts \  
--no-progress \  
--no-suggest \  
--no-interaction \  
--ansi "$@"' > /usr/bin/composer-require && \  
chmod +x /usr/bin/composer-require  

