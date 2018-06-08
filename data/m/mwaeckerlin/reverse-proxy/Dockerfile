FROM mwaeckerlin/letsencrypt  
MAINTAINER mwaeckerlin  
  
RUN apk add nginx inotify-tools openssl \  
&& mkdir -p /run/nginx \  
&& chown $WWWUSER /run/nginx  
  
ADD proxy.conf /etc/nginx/proxy.conf  
ADD ssl.conf /etc/nginx/conf.d/ssl.conf  
ADD nginx.conf /etc/nginx/nginx.conf  
RUN sed -i 's/\\(client_max_body_size\\).*;/\1 0;/' /etc/nginx/proxy.conf  
  
ADD error /etc/nginx/error  
ADD nginx-configure.sh /nginx-configure.sh  
ADD start.sh /start.sh  
  
# DEBUG_LEVEL is one of: debug, info, notice, warn, error, crit, alert, emerg  
# logs are written to /var/log/nginx/error.log and /var/log/nginx/access.log  
ENV DEBUG_LEVEL "error"  
ENV LDAP_HOST ""  
ENV LDAP_BASE_DN ""  
ENV LDAP_BIND_DN ""  
ENV LDAP_BIND_PASS ""  
ENV LDAP_REALM "Restricted"  
ENV BASIC_AUTH_REALM ""  
EXPOSE ${HTTP_PORT} ${HTTPS_PORT}  
ENTRYPOINT ["/start.sh"]  
  
VOLUME /etc/nginx/sites-available  
VOLUME /etc/nginx/sites-enabled  
VOLUME /etc/nginx/basic-auth  

