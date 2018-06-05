# Docker image that serves static content via NGINX, with autoindex enabled.  
FROM nginx:alpine  
MAINTAINER XSF Editors <editor@xmpp.org>  
COPY deploy/nginx.vh.default.conf /etc/nginx/conf.d/default.conf  
COPY content /usr/share/nginx/html  
RUN rm /usr/share/nginx/html/index.html  

