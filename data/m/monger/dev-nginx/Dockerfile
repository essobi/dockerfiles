FROM alpine:3.5  
RUN apk add --no-cache \  
bash \  
nginx \  
shadow \  
gettext \  
openssl  
  
COPY start.sh /opt/start.sh  
COPY nginx.conf /etc/nginx/  
COPY fastcgi_params /etc/nginx/fastcgi_params  
  
RUN sed -i -e 's/\r$//' /opt/start.sh  
RUN sed -i -e 's/\r$//' /etc/nginx/nginx.conf  
  
RUN chmod u+rx,g+rx,o+rx,a-w /opt/start.sh && \  
usermod -u 10777 nginx && \  
groupmod -g 10777 nginx && \  
mkdir -p /opt/ssl && \  
chown -R nginx:nginx /opt/ && \  
mkdir -p /nginx/tmp/ && \  
chown -R nginx:nginx /nginx/  
  
COPY sites /etc/nginx/sites-available/  
RUN sed -i -e 's/\r$//' /etc/nginx/sites-available/*.vhost  
RUN mkdir /etc/nginx/sites-enabled  
  
ENTRYPOINT ["/opt/start.sh"]  
CMD ["nginx", "-c", "/etc/nginx/nginx.conf", "-g", "daemon off;"]

