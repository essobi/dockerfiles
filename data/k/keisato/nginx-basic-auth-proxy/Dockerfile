from nginx:1.9  
MAINTAINER kei-sato@meeetol.com  
  
# install .htpasswd  
RUN apt-get update && apt-get install -y apache2-utils && apt-get clean  
  
ADD etc/nginx/ /etc/nginx/  
ADD opt/local/bin/prepare /opt/local/bin/  
  
CMD ["sh", "-c", "/opt/local/bin/prepare && nginx -g 'daemon off;'"]  

