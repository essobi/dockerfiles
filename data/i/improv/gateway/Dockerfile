FROM nginx  
MAINTAINER Ando Roots <ando@sqroot.eu>  
  
RUN rm -rf /etc/nginx/default.conf /usr/share/nginx/html  
  
COPY nginx/nginx.conf /etc/nginx/  
COPY nginx/conf.d /etc/nginx/conf.d/  
COPY nginx/include /etc/nginx/include  
COPY nginx/ssl /etc/letsencrypt/live/api.improv.ee

