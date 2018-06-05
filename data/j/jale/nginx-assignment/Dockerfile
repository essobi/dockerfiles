# author Jaromir Lebeda  
# I am going to extend/change an existing official alpine image from Docker
Hub  
FROM nginx:1.13.12-alpine  
  
# Change working directory to root of nginx webhost  
WORKDIR /usr/share/nginx/html  
  
# Copy very simple html page  
COPY index.html index.html  
COPY picard.gif picard.gif  
  
# Adding SSL support (change working directory)  
WORKDIR /etc/ssl/certs  
  
# Install openssl to generate self-signed certificate for localhost  
# and change nginx configs.  
# Not sure if it is better to generate certs and change config in RUN or  
# copy from outside dockerfile using COPY.  
RUN apk update --no-cache \  
&& apk add openssl \  
&& openssl req -nodes -newkey rsa:2048 -sha256 -x509 -days 30 -keyout
localhost.key -out localhost.crt -subj
'/C=US/ST=Anywhere/L=Anywhere/O=Localhost/CN=localhost'  
# && echo $'server { \n\  
# listen 80; \n\  
# listen 443 ssl; \n\  
# server_name localhost; \n\  
# ssl_certificate /etc/ssl/certs/localhost.crt; \n\  
# ssl_certificate_key /etc/ssl/certs/localhost.key; \n\  
# ssl_protocols TLSv1.2 TLSv1.1 TLSv1; \n\  
# location / { \n\  
# root /usr/share/nginx/html; \n\  
# index index.html index.htm; \n\  
# } \n\  
# error_page 500 502 503 504 /50x.html; \n\  
# }' > /etc/nginx/conf.d/default.conf  
  
COPY config/default.conf /etc/nginx/conf.d/default.conf  
  
# Expose ports (port 80 already exposed in my FROM)  
EXPOSE 80 443  
  
# CMD is defined in my FROM  
# CMD ["nginx" "-g" "daemon off;"]  
  
LABEL name=nginx-assignment version=dev \  
maintainer="Jaromir Lebeda <lebeda.jaromir@gmail.com>"  

