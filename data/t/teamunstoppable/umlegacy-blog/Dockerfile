FROM tutum/wordpress-stackable:latest  
MAINTAINER Antony John <antojk@gmail.com>  
  
# Add an initial data which will be automatically loaded when creating the
database for the first time  
ADD db-dump/videoupload.sql /initial_db.sql  
  
# Add custom themes, plugins and/or uploads  
ADD wp-content/plugins/ /app/wp-content/plugins/  
ADD wp-content/themes/ /app/wp-content/themes/  
ADD wp-content/uploads/ /app/wp-content/uploads/  
RUN chown www-data:www-data /app/wp-content -R  
  

