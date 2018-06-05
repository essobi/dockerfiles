FROM hypriot/rpi-alpine-scratch  
MAINTAINER Alexander Puzynia <werwolf.by@gmail.com>  
  
RUN apk update && \  
apk upgrade && \  
apk add nginx && \  
adduser -S www-data && \  
ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log && \  
chown -R www-data:www-data /var/lib/nginx  
  
CMD ["nginx", "-g", "daemon off;"]

