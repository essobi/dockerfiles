FROM nginx:1.11.9-alpine  
  
# Create directory where to store dhparam.pem  
RUN mkdir -p /etc/nginx/sites-available/skipass.site/ssl \  
# Install required dependencies  
&& apk add \--no-cache --virtual .build-deps openssl \  
# Generate dhparam.pem file  
&& openssl dhparam -rand - 2048 -out /etc/nginx/sites-
available/skipass.site/ssl/dhparam.pem \  
&& apk del .build-deps \  
# Remove the default Nginx configuration file  
&& rm -v /etc/nginx/nginx.conf  
  
# Copy configuration files  
COPY /config /etc/nginx/  

