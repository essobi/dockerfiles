FROM nginx:stable-alpine  
  
MAINTAINER David Verdejo <david.verdejo@bluekiri.com>  
  
RUN apk update && \  
apk upgrade && \  
apk add --update --no-cache \  
# for healthcheck  
curl && \  
rm -rf /var/cache/apk/* && \  
rm -rf /tmp/*  
  
ENV THUMBOR_SERVICE_NAME thumbor  
ENV THUMBOR_SERVICE_PORT 8000  
ADD conf/site-thumbor.tmpl /etc/nginx/conf.d/  
  
RUN rm /etc/nginx/conf.d/default.conf && \  
envsubst < "/etc/nginx/conf.d/site-thumbor.tmpl" > "/etc/nginx/conf.d/site-
thumbor.conf" && \  
rm /etc/nginx/conf.d/site-thumbor.tmpl  
  
HEALTHCHECK \--interval=5s --timeout=3s \  
CMD curl -f http://localhost/hc || exit 1  

