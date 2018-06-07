FROM cybe/ps-base:alpine36  
  
RUN apk --no-cache add nginx \  
&& cd /etc/nginx \  
&& mkdir sites/ \  
# Remove unnecessary files  
&& rm -rf modules/ conf.d/default.conf nginx.conf fastcgi.conf fastcgi_params
scgi_params uwsgi_params koi-utf koi-win win-utf \  
&& rm -rf /etc/logrotate.d/ \  
&& delgroup www-data \  
# Setup nginx user  
&& addgroup -g 99 -S www-data \  
&& addgroup nginx www-data  
  
COPY nginx.conf /etc/nginx/  
  
CMD ["nginx"]  

