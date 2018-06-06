FROM nginx:1.12-alpine  
  
COPY ./nginx.conf /etc/nginx/nginx.conf  
COPY ./nginx_azuracast.conf /etc/nginx/conf.d/azuracast.conf  
  
VOLUME /etc/nginx/conf.d/  
  
RUN apk add --no-cache openssl  
  
# SSL self-signed cert generation  
RUN mkdir -p /etc/nginx/ssl/  
RUN openssl req -new -nodes -x509 -subj
"/C=US/ST=Texas/L=Austin/O=IT/CN=localhost" \  
-days 365 -extensions v3_ca \  
-keyout /etc/nginx/ssl/ssl.key \  
-out /etc/nginx/ssl/ssl.crt  
  
# Generate the dhparam.pem file (takes a long time)  
RUN openssl dhparam -dsaparam -out /etc/nginx/dhparam.pem 4096  
  
VOLUME /var/www/letsencrypt  
VOLUME /etc/nginx/ssl  
  
# Add the LetsEncrypt-connection script  
COPY ./scripts/letsencrypt_connect /usr/bin/letsencrypt_connect  
RUN chmod a+x /usr/bin/letsencrypt_connect  
  
# Install Dockerize  
ENV DOCKERIZE_VERSION v0.6.1  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
EXPOSE 80 443  
STOPSIGNAL SIGTERM  
  
ENTRYPOINT ["dockerize","-wait","tcp://web:9000","-timeout","10s"]  
  
CMD ["nginx", "-g", "daemon off;"]

