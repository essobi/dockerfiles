# NGINX image with customization for project:  
# https://github.com/garystafford/tw-cn-ip-build-deploy  
FROM nginx:latest  
  
MAINTAINER Gary A. Stafford <garystafford@rochester.rr.com>  
  
LABEL version="1.2.0"  
COPY static.zip /tmp/static.zip  
COPY default.conf /etc/nginx/conf.d/default.conf  
COPY build_nginx_conf_production.sh /tmp/build_nginx_conf_production.sh  
COPY default-template.conf /tmp/default-template.conf  
  
RUN apt-get update -y && \  
apt-get install unzip nano -y && \  
unzip /tmp/static.zip -d /usr/share/nginx/  

