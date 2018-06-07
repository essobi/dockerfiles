FROM circleci/php:7.1-node-browsers  
RUN sudo apt-get install -y libpng-dev libicu-dev libjpeg62-turbo-dev && \  
sudo docker-php-ext-configure gd \--with-jpeg-dir=/usr/include/ && \  
sudo docker-php-ext-install -j$(nproc) gd pcntl intl zip pdo_mysql  

