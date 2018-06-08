FROM justincarter/alpine-lucee:latest  
  
MAINTAINER Justin Carter justin.w.carter@gmail.com  
  
# install nginx and supervisor  
RUN apk add --update \  
nginx \  
supervisor && \  
rm -rf /var/cache/apk/*  
  
# configuration  
COPY nginx/nginx.conf /etc/nginx/nginx.conf  
COPY nginx/default.conf /etc/nginx/conf.d/default.conf  
COPY supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 80  
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/conf.d/supervisord.conf"]  

