FROM nginx:stable-alpine  
MAINTAINER Clint Edwards <clint.j.edwards@gmail.com>  
  
COPY ./docker/nginx/clintjedwards.com.crt /etc/ssl/certs/personal_website.crt  
COPY ./docker/nginx/clintjedwards.com.key
/etc/ssl/private/personal_website.key  
  
RUN rm /etc/nginx/conf.d/default.conf  
COPY ./docker/nginx/nginx.conf /etc/nginx/conf.d/personal_website.conf  
  
ENTRYPOINT ["nginx", "-g", "daemon off;"]  

