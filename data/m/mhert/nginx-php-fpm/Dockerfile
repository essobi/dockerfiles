FROM nginx:1.13.1-alpine  
  
ENTRYPOINT ["/sbin/tini", "--", "/usr/local/bin/docker-entrypoint.sh"]  
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]  
  
ENV PHP_HOST ""  
ENV PHP_PORT ""  
ENV DOCUMENT_ROOT "/var/www/"  
ENV FRONT_CONTROLLER "index.php"  
RUN apk add --no-cache \  
tini  
  
COPY bin/ /usr/local/bin/  
COPY docker-entrypoint.d/ /etc/docker-entrypoint.d/  
  
COPY conf/etc /etc  

