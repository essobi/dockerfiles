FROM nginx:1.11-alpine  
  
ADD kegbot.conf /etc/nginx/conf.d/default.conf  
ADD nginx.conf /etc/nginx/nginx.conf  
  
VOLUME ["/kegbot-data"]  
EXPOSE 80  

