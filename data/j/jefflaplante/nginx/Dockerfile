FROM nginx:alpine  
  
MAINTAINER Jeff LaPlante <jeff.laplante@disney.com>  
  
RUN mkdir -p /var/www/html  
  
COPY default.conf /etc/nginx/conf.d/default.conf  
  
CMD ["nginx", "-g", "daemon off;"]  

