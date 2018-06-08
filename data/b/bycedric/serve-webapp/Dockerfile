FROM bycedric/serve  
  
LABEL maintainer 'Cedric van Putten <me@bycedric.com>'  
  
COPY ./nginx-webapp.conf /etc/nginx/conf.d/sites-template/webapp.conf  
  
CMD ["sh", "-c", "ngxsite template webapp && ngxsite enable webapp && nginx -g
'daemon off;'"]  

