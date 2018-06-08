FROM nubs/composer-build:latest  
  
MAINTAINER Spencer Rinehart <anubis@overthemonkey.com>  
  
# Add the project code to the correct spot  
ONBUILD COPY . /code  
  
# Install the dependencies  
ONBUILD RUN composer install --no-interaction  
  
# Override composer install CMD with one to execute the project  
CMD ["composer", "start"]  

