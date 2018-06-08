FROM simplific/nginx-php  
  
RUN apk update \  
&& apk add ca-certificates wget \  
&& update-ca-certificates  
  
ENV PROCESSMAKER_VERSION 3.1.3  
RUN wget
http://downloads.sourceforge.net/project/processmaker/ProcessMaker/${PROCESSMAKER_VERSION}/processmaker-${PROCESSMAKER_VERSION}-community.tar.gz
-P /opt/  
RUN echo 'server { \  
listen 80 default_server; \  
server_name localhost; \  
\  
root /opt/processmaker/workflow/public_html; \  
\  
index index.html; \  
rewrite ^/(.*)$ /app.php last; \  
\  
location / { \  
try_files $uri =404; \  
} \  
\  
include php; \  
}' > /etc/nginx/conf.d/01-processmaker.conf  
  
RUN mkdir /opt/processmaker \  
&& tar -zxf /opt/processmaker-${PROCESSMAKER_VERSION}-community.tar.gz -C
/opt/ --overwrite  
  
RUN chown -R nginx:www-data /opt/processmaker/workflow && chown -R nginx:www-
data /opt/processmaker/shared  
  
RUN apk update && apk upgrade && apk add php && apk --no-cache --update add
php curl php-ctype php-cli php-curl php-soap php-ldap php-dom php-mysql
freetds php-mssql \  
&& cd /opt/processmaker/workflow/engine \  
&& rm -rf /var/cache/apk/*  
  
RUN ln -s ../../gulliver/bin/gulliver gulliver  
RUN echo "*/5 * * * * php -f /opt/processmaker/workflow/engine/bin/cron.php
+force" >> /var/spool/cron/crontabs/root  
  
VOLUME "/opt/processmaker/"  
WORKDIR "/opt/processmaker/workflow/engine"  

