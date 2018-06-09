FROM stenote/docker-lemp:latest  
  
COPY mysql.php /var/www/mysql.php  
COPY default /etc/nginx/sites-enabled/default  
RUN service nginx restart  

