FROM nginx:alpine  
  
RUN apk add --no-cache apache2-utils openssl  
  
COPY nginx/ /etc/nginx/  
COPY bin/ /usr/local/bin/  
  
CMD "nginx"  
  
EXPOSE 443  

