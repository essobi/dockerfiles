##  
## SmartVISU  
##  
## Use latest nginx Alpine based images as starting point  
FROM php:7-fpm-alpine  
  
ARG SHNG_SMARTVISU_BRANCH=master  
ENV SHNG_SMARTVISU_BRANCH=$SHNG_SMARTVISU_BRANCH  
  
## Images labels  
LABEL version = $SHNG_SMARTVISU_BRANCH \  
description = "SmartVisu image"  
maintainer = "Serge Wagener serge@wagener.family"  
COPY entrypoint.sh /  
  
## Install NGINX and GIT  
RUN mkdir -p /etc/nginx \  
&& apk add --no-cache git nginx \  
&& chmod a+x /entrypoint.sh  
  
COPY nginx.conf /etc/nginx  
  
## SmartVISU web interface  
EXPOSE 80 443  
## Make SmartVISU "mountable" by end user  
VOLUME /var/www/html  
  
ENTRYPOINT ["/entrypoint.sh"]  

