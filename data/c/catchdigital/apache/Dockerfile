FROM httpd:2.4.29  
MAINTAINER Liam Hiscock  
  
RUN echo "Include conf/conf.d/*.conf" >> /usr/local/apache2/conf/httpd.conf  
RUN apt-get update && apt-get install -y \  
libapache2-mod-proxy-html  
  
  
RUN set -ex; \  
mkdir -p /usr/local/apache2/conf/conf.d  
COPY templates/conf/conf.d/vhost.conf
/usr/local/apache2/conf/conf.d/vhost.conf  
COPY templates/conf/httpd.conf /usr/local/apache2/conf/httpd.conf  
  
WORKDIR /var/www/html  
  

