FROM ulsmith/alpine-apache-php7  
  
MAINTAINER Jan Ritter - janrtr <git@janrtr.de>  
  
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf  
  
COPY application/ /app/public/v1/application  
COPY system/ /app/public/v1/system  
COPY predis/ /app/public/v1/predis  
COPY index.php /app/public/v1/index.php  
COPY .htaccess /app/public/v1/.htaccess  
  
EXPOSE 80  
HEALTHCHECK CMD curl localhost/v1/station/name/heumarkt || exit 1  
ENTRYPOINT ["/bootstrap/start.sh"]  

