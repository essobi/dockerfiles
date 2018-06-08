FROM pataquets/apache-drupal:trusty  
  
RUN \  
rm /var/www/html/index.html && \  
cd /var/www/html && \  
git clone --single-branch --branch 7.x
http://git.drupal.org/project/drupal.git .  
  
RUN \  
chown -vR www-data:www-data \  
/var/www/html/sites/all \  
/var/www/html/sites/default  

