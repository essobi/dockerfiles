FROM wolnosciowiec/docker-php-fpm-node-glibc6:chromium  
  
ENV APP_VERSION=1  
# application configuration  
ENV FP_SKIPPED_HEADERS "content-length,host,connection,accept-
encoding,x-frontend-prerenderer,user-agent"  
ENV FP_ALLOWED_DOMAINS
"facebook.com,web.facebook.com,www.facebook.com,www.web.facebook.com,application"  
ENV FP_DELAY 0  
ENV FP_TIMEOUT 0  
ENV FP_WITH_IMAGES 0  
ENV FP_DEBUG 0  
ENV FP_RENDERER "chromium"  
ENV FP_CHROMIUM_BINARY "chromium-browser"  
ENV FP_WINDOW_SIZE "1920x1080"  
ENV FP_OPEN_PROCESS_LIMIT 3  
ENV FP_WAIT_FOR_PROCESS_TIME 4  
RUN apt update && apt install nginx -y  
  
ADD docker/common/etc/crontab /etc/crontabs/node  
ADD docker/common/entrypoint-prerenderer.sh /entrypoint-prerenderer.sh  
ADD docker/common/etc/nginx/nginx.conf /etc/nginx/nginx.conf  
ADD docker/common/etc/nginx/sites-enabled/default /etc/nginx/sites-
enabled/default  
ADD docker/common/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN chmod +x entrypoint-prerenderer.sh  
  
# add the whole application  
ADD . /www/frontend-prerenderer  
  
EXPOSE 80  
EXPOSE 9000  
ENTRYPOINT ["/entrypoint-prerenderer.sh"]  

