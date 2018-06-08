FROM alpine  
  
MAINTAINER Paul Urban  
  
RUN apk add --update nginx \  
&& echo "daemon off;" >> /etc/nginx/nginx.conf  
  
ONBUILD RUN rm -rf /etc/nginx/conf.d/*  
ONBUILD COPY src/www.conf /etc/nginx/conf.d/www.conf  
ONBUILD COPY src/nginx.conf /etc/nginx/nginx.conf  
ONBUILD ADD src/html /app/html  
  
EXPOSE 80 443  
CMD [ "/usr/sbin/nginx" ]  

