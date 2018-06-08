FROM nginx  
  
LABEL maintainer="Snakebot"  
  
RUN apt-get update && apt-get install -y openssl letsencrypt python-certbot-
nginx apache2-utils  
VOLUME [ "/data" ]  
VOLUME [ "/etc/nginx" ]  
  

