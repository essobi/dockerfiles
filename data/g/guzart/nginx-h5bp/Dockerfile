FROM 'nginx:1.12.2-alpine'  
  
RUN apk \--update add \--no-cache \--virtual .build-deps git \  
&& git clone https://github.com/h5bp/server-configs-nginx.git nginx-configs \  
&& apk del .build-deps \  
&& cp /etc/nginx/conf.d/default.conf nginx-configs/sites-available/default \  
&& rm -rf /etc/nginx \  
&& mv nginx-configs /etc/nginx \  
&& sed -i 's/user *www *www;/user nginx;/g' /etc/nginx/nginx.conf \  
&& sed -i 's/worker_processes *auto;/worker_processes 1;/g'
/etc/nginx/nginx.conf \  
&& sed -i 's/error_log .*;/error_log \/var\/log\/nginx\/error.log warn;/g'
/etc/nginx/nginx.conf \  
&& sed -i 's/access_log .*;/access_log \/var\/log\/nginx\/access.log main;/g'
/etc/nginx/nginx.conf \  
&& ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default \  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80  
  
STOPSIGNAL SIGTERM  
  
CMD ["nginx", "-g", "daemon off;"]

