FROM nginx:1.13-alpine  
  
# Copy the config files.  
COPY ./nginx.conf /etc/nginx/nginx.conf  
COPY ./fastcgi_params /etc/nginx/fastcgi_params  
  
VOLUME ["/etc/nginx/conf.d", "/var/code"]  

