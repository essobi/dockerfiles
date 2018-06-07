FROM php:7.0.7  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
&& \  
php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'aa96f26c2b67226a324c27919f1eb05f21c248b987e6195cad9690d5c1ff713d53020a02ac8c217dbf90a7eacc9d141d')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" && \  
php composer-setup.php --install-dir=/usr/local/bin --filename=composer && \  
php -r "unlink('composer-setup.php');"  
  
RUN apt-get update && \  
apt-get install -y git sudo unzip zip  
  
RUN composer global require "hirak/prestissimo:^0.3"  
RUN composer global require pantheon-systems/terminus ">=0.13.3"  
  
RUN mkdir -p ~/terminus/plugins && \  
git clone https://github.com/greg-1-anderson/terminus-secrets-plugin
~/terminus/plugins/terminus-secrets-plugin  
  
ENV PATH "$PATH:/root/.composer/vendor/bin"  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

