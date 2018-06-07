FROM kyma/docker-nginx  
  
COPY ./_site/ /var/www/  
COPY ./default /etc/nginx/sites-enabled/default  
  
RUN chmod -R 755 /var/www/  
  
CMD 'nginx'  
  

