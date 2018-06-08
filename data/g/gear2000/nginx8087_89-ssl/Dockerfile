FROM gear2000/nginx  
MAINTAINER Gary Leong <gwleong@gmail.com>  
  
ADD sites-enabled/ /etc/nginx/sites-enabled/  
  
#ADD app/ /app/  
#RUN openssl req -newkey rsa:2048 -new -x509 -subj
"/C=US/ST=California/L=SanFrancisco/O=Dis/CN=www.selfsigned.com" -days 1024
-nodes -out /etc/ssl/certs/nginx.crt -keyout /etc/ssl/certs/nginx.key && \  
# bash -c 'cat /etc/ssl/certs/nginx.crt /etc/ssl/certs/nginx.key >
/etc/ssl/certs/nginx.pem'  
RUN openssl req -newkey rsa:2048 -new -x509 -subj
"/C=US/ST=California/L=SanFrancisco/O=Dis/CN=www.selfsigned.com" -days 1024
-nodes -out /etc/ssl/certs/nginx.crt -keyout /etc/ssl/private/nginx.key  
  
RUN openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048  
  
EXPOSE 8089 8087  
CMD ["nginx", "-g", "daemon off;"]  
  

