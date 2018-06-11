FROM nginx:1.11.4-alpine  
  
# Install tzdata and change to Europe/Paris  
RUN set -x && \  
apk --update add tzdata logrotate && \  
ln -sf /usr/share/zoneinfo/Europe/Paris /etc/localtime && \  
rm -rf /var/cache/apk/*  
  
# Install tools...  
RUN set -x && \  
apk --update add \  
ca-certificates \  
nano \  
openssl \  
openssh-client \  
acl \  
bash \  
&& rm -rf /var/cache/apk/*  
  
# Custom nginx configuration  
COPY nginx/nginx.conf /etc/nginx/nginx.conf  
COPY nginx/default.conf /etc/nginx/conf.d/default.conf  
  
# Custom logrotate configuration for nginx  
COPY logrotate/nginx /etc/logrotate.d/nginx  
COPY logrotate/cron /etc/periodic/daily/logrotate-cron  
  
# Custom entry point  
COPY scripts/start.sh /root/start.sh  
  
RUN chmod +x /root/start.sh \  
&& chmod +x /etc/periodic/daily/logrotate-cron  
  
WORKDIR /var/www/html  
CMD ["/root/start.sh"]  

