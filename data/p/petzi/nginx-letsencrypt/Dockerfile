FROM nginx:1.13-alpine  
  
# certbot from letsencrypt  
# gettext for envsubst  
# openssl for self-signed certificates in dev mode  
RUN apk add --no-cache \  
certbot \  
openssl  
  
VOLUME /etc/letsencrypt/  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["nginx"]  
RUN rm /etc/nginx/conf.d/default.conf  
  
COPY lib/ /usr/local/lib  
COPY extlib/log4sh/log4sh /usr/local/lib  
COPY extlib/shflags/shflags /usr/local/lib  
  
COPY bin/ /usr/local/bin  
RUN chmod u+x /usr/local/bin/*.sh  
RUN ln -s /usr/local/bin/entrypoint.sh /entrypoint.sh  
RUN ln -s /usr/local/bin/cert-renew.sh /cert-renew.sh  
RUN ln -s /usr/local/bin/backend-reconfigure.sh /backend-reconfigure.sh  

