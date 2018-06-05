FROM socketwench/drupal-base:8  
MAINTAINER tess@deninet.com  
  
ADD http://xdebug.org/files/xdebug-2.4.0.tgz /tmp/xdebug-2.4.0.tgz  
  
RUN cd /tmp && \  
tar -xzf xdebug-2.4.0.tgz && \  
cd xdebug-2.4.0 && \  
phpize && \  
./configure && \  
make && \  
cp modules/xdebug.so /usr/local/lib/php/extensions/xdebug.so  
  
# Add custom PHP configuration changes from php.ini  
COPY php.ini /usr/local/etc/php/  

