FROM nginx:mainline-alpine  
MAINTAINER Karl Fathi <karl@pixelfordinner.com>  
  
ENV LANG C.UTF-8  
RUN rm /etc/nginx/nginx.conf && \  
rm /etc/nginx/fastcgi_params && \  
rm -rf /etc/nginx/conf.d && \  
rm -rf /etc/nginx/vhost.d && \  
mkdir -p /etc/nginx/conf.d && \  
mkdir -p /etc/nginx/vhost.d  
  
COPY data/boilerplate/ /etc/nginx/boilerplate/  
COPY data/nginx.conf /etc/nginx/  
COPY data/proxy.conf /etc/nginx/  
COPY data/fastcgi_params /etc/nginx/  
COPY data/mime.types /etc/nginx/  
  
VOLUME ["/var/cache/nginx"]  
  
EXPOSE 80 443  
CMD ["nginx"]  

