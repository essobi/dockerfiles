FROM nginx:latest  
MAINTAINER Muscle Cars <hello@musclecars.fr>  
  
COPY www /var/www/  
  
RUN rm /etc/nginx/conf.d/default.conf  
COPY musclecars.fr.conf /etc/nginx/conf.d/  
  
CMD ["nginx", "-g", "daemon off;"]  

