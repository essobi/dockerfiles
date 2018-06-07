FROM nginx:latest  
  
ENV RELOADER_VERSION=0.1.2-alpha  
  
ADD
https://github.com/honsiorovskyi/nginx_reloader/releases/download/$RELOADER_VERSION/nginx_reloader
\  
/usr/local/bin/nginx_reloader  
  
RUN chmod +x /usr/local/bin/nginx_reloader  
  
EXPOSE 4567  
CMD /usr/local/bin/nginx_reloader --port 4567 \  
& nginx -g "daemon off;"  

