FROM nginx:1.13-alpine  
  
COPY html /usr/share/nginx/html  
COPY ./nginx.conf /etc/nginx/nginx.conf  
  
COPY ./certs/mycert.crt /etc/ssl/mycert.crt  
COPY ./certs/mykey.key /etc/ssl/mykey.key  
#RUN chown -R nginx:nginx /usr/share/nginx/html  
  
EXPOSE 443

