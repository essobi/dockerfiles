FROM circleci/php:7.1-cli-node-browsers  
  
ENV APP_ENV=ci  
ENV CI=true  
ENV APP_DEBUG=true  
RUN sudo apt-get update  
RUN sudo apt-get install -f -y --force-yes ghostscript libmagickwand-6.q16-dev
libmagickcore-6.q16-dev librsvg2-dev libglib2.0-dev libgdk-pixbuf2.0-dev
libcairo2-dev libglib2.0-0=2.42.1-1+b1 libglib2.0-bin=2.42.1-1+b1 ghostscript
libgs9 libcupsimage2 libcups2=1.7.5-11+deb8u2  
RUN printf "yes\n" | sudo pecl install imagick-3.4.3  
RUN sudo docker-php-ext-enable imagick  
RUN sudo apt-get install -y libmcrypt-dev libpng-dev libpq-dev  
RUN sudo docker-php-ext-install gd mcrypt pdo pdo_pgsql zip  
RUN sudo docker-php-ext-enable gd mcrypt pdo pdo_pgsql zip  

