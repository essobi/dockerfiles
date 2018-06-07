FROM unocha/alpine-nginx-extras:201610-PR95  
  
RUN mkdir -p /srv/www  
  
COPY ./html /srv/www/html/  
  
COPY ./conf/nginx/default.conf /etc/nginx/conf.d/  

