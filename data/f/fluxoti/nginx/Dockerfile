FROM nginx:1.10.0-alpine  
MAINTAINER Fluxoti <lucas.gois@fluxoti.com>  
  
COPY . /build  
  
ENV PHP_FPM_HOST=php PHP_FPM_PORT=9000  
RUN cp /build/virtualhost /etc/nginx/conf.d/default.conf \  
&& cp /build/nginx.conf /etc/nginx/nginx.conf \  
&& cp /build/nginx-entrypoint.sh /nginx-entrypoint.sh && chmod +x /nginx-
entrypoint.sh  
  
CMD ["/nginx-entrypoint.sh"]  

