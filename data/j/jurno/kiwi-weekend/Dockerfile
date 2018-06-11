FROM nginx:alpine  
RUN apk --no-cache add openssl bash  
  
COPY ./website /usr/share/nginx/html  
COPY ./nginx-conf/nginx.conf /etc/nginx/nginx.conf  
COPY ./letsencrypt/ssl-cert.sh /etc/ssl  
  
WORKDIR /etc/ssl  
RUN chmod u+x ssl-cert.sh  
RUN ./ssl-cert.sh  
  
EXPOSE 80 443

