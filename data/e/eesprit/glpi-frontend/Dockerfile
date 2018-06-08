FROM nginx:1.11.1-alpine  
  
ENV GLPI_VERSION=0.90.4  
RUN apk upgrade --update \  
&& apk add curl \  
&& curl -L https://github.com/glpi-
project/glpi/releases/download/${GLPI_VERSION}/glpi-${GLPI_VERSION}.tar.gz -o
/tmp/glpi.tar.gz \  
&& tar xvfz /tmp/glpi.tar.gz -C /usr/share/nginx/ \  
&& rm -f /tmp/glpi.tar.gz \  
&& apk del curl \  
&& rm -rf /var/cache/apk/*  
  
ADD php-fpm.conf /etc/nginx/conf.d  
ADD fastcgi_fpm.conf /etc/nginx/snippets/fastcgi_fpm.conf  
ADD server.conf /etc/nginx/conf.d/default.conf  

