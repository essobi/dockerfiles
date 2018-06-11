FROM nginx:alpine  
  
COPY ./conf.d/nginx.conf /etc/nginx/nginx.conf  
COPY ./conf.d/default.conf /etc/nginx/conf.d/default.conf  
COPY ./conf.d/health_check.conf /etc/nginx/conf.d/health_check.conf  
  
WORKDIR /var/www  

