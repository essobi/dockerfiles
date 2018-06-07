  
# Needs alpine:3.3 or later to have --no-cache support  
FROM alpine  
MAINTAINER Sven Dowideit <SvenDowideit@home.org.au>  
  
# This is enoughtfor the transformed version  
RUN apk add --no-cache nginx wget \  
&& rm -rf /var/cache/apk/* \  
&& nginx -V  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
VOLUME ["/var/cache/nginx"]  
EXPOSE 80 443  
ENTRYPOINT ["nginx", "-g", "daemon off;"]  
  
# And then add your files to /usr/share/nginx/html/  

