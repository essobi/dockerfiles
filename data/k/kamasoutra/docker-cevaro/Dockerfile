FROM nginx:alpine  
  
LABEL maintainer="Jean-Pierre Palik - kama@palik.fr" \  
description="Sources from cevaro.eu" \  
version="1.0"  
  
COPY . /usr/share/nginx/html  
  
RUN mv /usr/share/nginx/html/default.conf /etc/nginx/conf.d/default.conf  

