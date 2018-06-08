FROM wodby/nginx:1.10  
ENV WODBY_DIR_FILES /mnt/files  
  
RUN rm /etc/gotpl/default-vhost.conf.tpl && \  
mkdir -p $WODBY_DIR_FILES  
  
COPY neuffer.conf.tpl /etc/gotpl/  
  
COPY test/.htpasswd /etc/nginx/  
  
COPY init/* /docker-entrypoint-init.d/  

