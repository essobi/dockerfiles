FROM nginx:1.13.12-alpine  
ENV MAGE_ROOT=/var/www/html \  
MAGE_HOST=phpfpm  
COPY default.conf.template /etc/nginx/conf.d/default.conf.template  
COPY docker-nginx-entrypoint /usr/local/bin  
ENTRYPOINT ["docker-nginx-entrypoint"]  
CMD ["nginx", "-g", "daemon off;"]  

