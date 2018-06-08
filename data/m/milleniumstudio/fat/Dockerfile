FROM nginx:latest  
MAINTAINER FAT <contact@fat.sh>  
  
COPY . /var/www/  
  
RUN rm /etc/nginx/conf.d/default.conf  
COPY contrib/fat.conf /etc/nginx/conf.d/  
  
CMD ["nginx", "-g", "daemon off;"]  

