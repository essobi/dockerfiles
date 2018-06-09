FROM quantumobject/docker-alpine  
  
RUN apk --update add nano git zip unzip openssl \  
php7 php7-phar php7-json php7-mbstring php7-openssl \  
nodejs-current nodejs-current-npm  
RUN wget https://getcomposer.org/composer.phar && chmod +x composer.phar && mv
composer.phar /usr/local/bin/composer  
RUN wget -q https://github.com/pupper/pupper/archive/master.zip; exit 0  
RUN unzip master.zip  
WORKDIR pupper-master  
RUN composer install -o --no-dev  
RUN npm i  
RUN npm run build  
  
CMD npm start  

