FROM cscadehub/lib-base-backend:latest  
  
COPY ./ /var/www/html  
  
RUN mv /var/www/html/.env.cloud.dev /var/www/html/.env  
  
RUN chmod -R 777 /var/www/html/bootstrap && chmod -R 777 /var/www/html/storage
&& chmod -R 777 /var/www/html/app/Base  
  
RUN php artisan optimize  
  
RUN php artisan key:generate  
  
CMD ["php", "artisan", "migrate:refresh", "--seed"]  
  

