FROM nginx:1.12-alpine  
MAINTAINER Secopstech <info@secops.tech>  
ENV ENDPOINT=NON_DEFINED_ENDPOINT  
  
WORKDIR /usr/share/nginx/html  
COPY endpoint.html /usr/share/nginx/html  
  
CMD cd /usr/share/nginx/html && sed -e s/NON_DEFINED_ENDPOINT/"$ENDPOINT"/
endpoint.html > index.html ; nginx -g 'daemon off;'  

