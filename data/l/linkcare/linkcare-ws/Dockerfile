FROM linkcare/linkcaredockerservers:Complete_1  
EXPOSE 80  
WORKDIR /var/www/html  
COPY composer.json ./  
RUN composer install --prefer-source --no-interaction  
  
# Generate php file with system texts translations  
WORKDIR /var/www/html  
COPY . ./  
RUN chmod 777 tmp  
RUN php migrate/generate_locale.php migrate/description/system.new.htm >
resources/Locale.Class.php  
  
RUN mkdir docs && mkdir /var/www/export && chmod 777 docs && chmod 777
/var/www/export  

