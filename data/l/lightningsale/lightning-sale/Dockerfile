FROM richard87/php-base  
  
WORKDIR /var  
RUN rm -Rf /var/www  
  
RUN git clone \--depth=1 --branch=master
https://github.com/lightningsale/LightningSale.git /var/www \  
&& rm -Rf /var/www/.git  
WORKDIR /var/www  
  
RUN composer install --no-scripts --no-autoloader  
RUN composer dump-autoload -o  
  
ENV APP_ENV=prod \  
APP_DEBUG=false \  
APP_SECRET=22375fd9fdfe7235fb7386334f6e9632 \  
DATABASE_URL=mysql://root:abcd1234@mysql:3306/lightningsale \  
LND_HOST=lnd \  
LND_PORT=8080 \  
EXTERNALIP=92.221.98.237 \  
EXTERNALPORT=9736 \  
RPCUSER=lightningsale \  
RPCPASS=lightningsale \  
NETWORK=testnet \  
CHAIN=bitcoin \  
DEBUG=info \  
REDIS_URL=redis  
  
RUN php bin/console cache:warmup

