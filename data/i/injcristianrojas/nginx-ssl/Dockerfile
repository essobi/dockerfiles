FROM nginx:1.7.12  
  
RUN openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048  
RUN openssl req -nodes -new -newkey rsa:4096 -out server.csr -sha256 \  
-subj "/C=CL/ST=Santiago/L=Santiago/O=MySecurity/OU=IT Department/CN=localhost"  
RUN mv privkey.pem /etc/ssl/private/server.key  
RUN openssl x509 -req -days 365 -sha256 -in server.csr \  
-signkey /etc/ssl/private/server.key -out /etc/ssl/certs/server.crt  
COPY default.conf /etc/nginx/conf.d/default.conf  

