FROM drupal  
RUN apt-get update  
RUN ["apt-get", "install", "-y", "vim"]  
RUN chown -R www-data:www-data /var/www/html/sites/default  
RUN chmod -R 700 /var/www/html/sites/default  
RUN /bin/bash -c "cp /var/www/html/sites/default/default.settings.php
/var/www/html/sites/default/settings.php"  

