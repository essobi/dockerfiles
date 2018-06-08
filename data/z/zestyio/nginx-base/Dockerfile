FROM nginx:1.12-alpine  
  
CMD /usr/sbin/nginx -c /etc/nginx/nginx.conf -g "${NGINX_DIRECTIVES-}"  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY nginx-main.conf /etc/nginx/nginx-main/base.conf  
COPY nginx-events.conf /etc/nginx/nginx-events/base.conf  
COPY nginx-http.conf /etc/nginx/nginx-http/base.conf  
  
RUN find /etc/nginx/conf.d -type f -delete && \  
chown -R guest /var/run  
  
USER guest  

