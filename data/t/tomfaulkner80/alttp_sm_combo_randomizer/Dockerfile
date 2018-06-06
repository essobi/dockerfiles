FROM alexpfishvision/ubuntu-php7-composer  
RUN apt-get update && apt-get install -y php7.1-bcmath  
  
WORKDIR /usr/app  
RUN git clone https://github.com/tewtal/alttp_sm_combo_randomizer.git  
WORKDIR /usr/app/alttp_sm_combo_randomizer  
RUN mv .env.example .env  
  
RUN composer install  
VOLUME /rom  
ENTRYPOINT ["php", "artisan", "alttp:randomize"]  

