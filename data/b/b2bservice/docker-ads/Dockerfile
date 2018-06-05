FROM php:5.6-fpm  
  
COPY entrypoint.sh entrypoint.sh  
COPY composer-install.sh composer-install.sh  
COPY install.sh install.sh  
  
RUN chmod +x install.sh composer-install.sh && ./install.sh && rm -rf
install.sh composer-install.sh  
  
WORKDIR /var/www  
  
CMD [./entypoint.sh]

