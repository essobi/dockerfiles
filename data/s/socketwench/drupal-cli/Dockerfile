FROM socketwench/drupal-cli:base  
MAINTAINER tess@deninet.com  
  
# Manually install Drupal Console due to
https://github.com/hechoendrupal/DrupalConsole/issues/2064  
RUN curl https://drupalconsole.com/installer -L -o drupal.phar && \  
chmod +x drupal.phar && \  
mv drupal.phar /usr/bin/drupal  
  
# Download xdebug  
ADD http://xdebug.org/files/xdebug-2.4.0.tgz /tmp/xdebug-2.4.0.tgz  
  
# Install xdebug  
RUN cd /tmp && \  
tar -xzf xdebug-2.4.0.tgz && \  
cd xdebug-2.4.0 && \  
phpize && \  
./configure && \  
make && \  
cp modules/xdebug.so /usr/local/lib/php/extensions/xdebug.so  
  
# Add custom PHP configuration changes from php.ini  
COPY php.ini /usr/local/etc/php/  
  
WORKDIR /var/www/html  

