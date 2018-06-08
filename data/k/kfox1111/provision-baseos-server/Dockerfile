# Copy everything from nginx-alpine into data container to invert the layers.  
# This allows the server to be updated without repulling the data layer.  
FROM nginx:alpine  
RUN echo hi  
  
FROM kfox1111/provision-baseos:centos-7-1708-x86_64  
COPY \--from=0 / /  
  
# Force everything to be a download.  
RUN echo "server {autoindex off; server_name localhost; location ~ ^/$ {return
200;} location ~ ^.*/$ {return 404;} location / { root /data; default_type
application/octet-stream; add_header Content-Disposition 'attachment'; types
{}}}" > /etc/nginx/conf.d/default.conf  
  
EXPOSE 80  
STOPSIGNAL SIGTERM  
CMD ["nginx", "-g", "daemon off;"]  

