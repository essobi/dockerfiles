FROM nginx:alpine  
  
ENV EMAIL your@mail.addr  
ENV DOMAIN server.tld  
  
ADD default.conf /etc/nginx/conf.d/default.conf  
ADD openldap.conf /etc/nginx/example/openldap.conf  
ADD nextcloud.conf /etc/nginx/example/nextcloud.conf  
ADD crontab /var/spool/cron/crontabs/certbot-renew  
ADD entrypoint.sh /entrypoint.sh  
  
RUN apk update \  
&& apk add --no-cache certbot acme-client openssl ca-certificates \  
&& rm -rf /var/cache/apk/* \  
&& chmod 711 /entrypoint.sh \  
&& mkdir -p /usr/share/nginx/html/.well-known/acme-challagme  
  
VOLUME /etc/letsencrypt  
VOLUME /etc/nginx/conf.d  
EXPOSE 80 443  
CMD ["/entrypoint.sh"]  

