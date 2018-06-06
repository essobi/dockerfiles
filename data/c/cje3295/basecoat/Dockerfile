FROM nginx:stable-alpine  
MAINTAINER Clint Edwards <clint.j.edwards@gmail.com>  
  
COPY ./docker/nginx/star.clintjedwardslocal.com.crt
/etc/ssl/certs/basecoat.crt  
COPY ./docker/nginx/star.clintjedwardslocal.com.key
/etc/ssl/private/basecoat.key  
  
RUN rm /etc/nginx/conf.d/default.conf  
COPY ./docker/nginx/nginx.conf /etc/nginx/conf.d/basecoat.conf  
  
ENTRYPOINT ["nginx", "-g", "daemon off;"]  

