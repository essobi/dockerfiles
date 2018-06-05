FROM analogic/sym4server  
  
ENV APP_ENV dev  
ENV APP_SECRET 6373e1ace63596295cf602efa7772996  
ENV CLIGHTNING_RPC_SOCKET unix:///root/.lightning/lightning-rpc  
ENV BITCOIND_RPC_DSN http://bitcoinrpc:rpcpassword@regnet:18334  
ENV PASSWORD admin  
ENV SESSION_NAME clightning  
  
ADD . /var/www/  
ADD rootfs /  
  
RUN cd /var/www && \  
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \  
php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" && \  
php composer-setup.php && \  
php -r "unlink('composer-setup.php');" && \  
php composer.phar install && \  
rm composer.phar

