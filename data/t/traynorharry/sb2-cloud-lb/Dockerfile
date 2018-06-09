FROM nginx:stable  
MAINTAINER harry@sb2.team  
  
##################### LB SETUP #####################  
  
# copy config for Nginx  
COPY nginx.conf /etc/nginx/nginx.conf  
  
# set directory for SSL & Cache  
RUN mkdir -p /etc/nginx/ssl  
RUN mkdir -p /var/cache/nginx  
RUN mkdir -p /var/tmp  
  
# set working directory  
WORKDIR /etc/nginx/ssl  
  
# copy SSL certs  
COPY sb2_cloud.crt /etc/nginx/ssl/sb2_cloud.crt  
COPY sb2_cloud.key /etc/nginx/ssl/sb2_cloud.key  
  
##################### INSTALLATION END #####################  
  
# set default port  
EXPOSE 80 443 8080 8081  

