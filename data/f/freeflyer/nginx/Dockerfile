FROM alpine:3.5  
  
MAINTAINER Nicolas Zagulajew (freeeflyer) <docker.com@xoop.org>  
  
  
RUN apk add --update nginx nginx-mod-http-fancyindex supervisor \  
&& rm -rf /var/cache/apk/* \  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log \  
&& mkdir -p /var/nginx \  
&& mkdir -p /run/nginx \  
&& mkdir -p /var/supervisor.d  
  
ADD nginx_supervisord.ini /etc/supervisor.d/nginx.ini  
  
EXPOSE 80 443  
  
CMD ["supervisord", "-n", "-c", "/etc/supervisord.conf" ]  
#CMD ["nginx", "-g", "daemon off;" ]  

