#  
# Dockerfile for nginx  
#  
FROM alpine  
  
MAINTAINER jovi <noreply@jovipro.com>  
  
RUN set -xe \  
&& apk add --no-cache nginx \  
&& mkdir -p /run/nginx  
  
EXPOSE 80  
CMD ["nginx", "-g", "daemon off;"]  

