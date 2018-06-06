FROM hitalos/laravel  
MAINTAINER rubensteen <rubensteen123@gmail.com>  
  
RUN git config --system http.sslverify false  
  
RUN git clone
https://d0f8c5458144c39e46a0c07904542a798104eb25@github.com/Cruorzy/laravel.git
/var/www  
  
RUN cp .env.production .env  
  
# Run Composer Install  
RUN composer install -d /var/www  
RUN php /var/www/artisan key:generate  
  
WORKDIR /var/www  
  
CMD php ./artisan serve --port=80 --host=0.0.0.0  
EXPOSE 80  

