FROM nginx:1.14  
ARG TAG  
LABEL TAG=${TAG}  
  
ENV TINI_VERSION v0.18.0  
ENV RESOLVER=none  
ENV RESOLVER_VALID=30s  
ENV SERVERNAME=localhost  
  
ENV SSL_CERT=/certs/fullchain.crt  
ENV SSL_CERT_KEY=/certs/fullchain.key  
ENV FPM_STATIC_WEBROOT=/var/www/web/  
ENV ENABLE_CONDITIONAL_BASIC_AUTH="NO"  
ENV KEEPALIVE_TIMEOUT=200  
ENV PROXY_STANDARD_FORWARD_PROTO="\$scheme"  
ENV PROXY_STANDARD_FORWARD_PORT="\$server_port"  
ENV GZIP_ENABLED="on"  
ENV GZIP_TYPES="text/css text/plain text/javascript application/javascript
application/json application/x-javascript text/xml application/xml
application/xml+rss application/xhtml+xml application/x-font-ttf
application/x-font-opentype application/vnd.ms-fontobject image/svg+xml
image/x-icon application/rss+xml application/atom_xml text/x-gettext-
translation"  
# envs for conditional basic auth settings  
ENV CONDITIONAL_BASIC_AUTH_HEADER="http_x_forwarded_for"  
ENV CONDITIONAL_BASIC_AUTH_REGEX="~172\\..*"  
ENV EXPOSE_PATH "/"  
ENV ENVIRONMENT_JSON_PREFIX "ADMIN_"  
ENV DEFAULT_SERVE "none"  
ADD src /  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y apache2-utils && \  
apt-get clean && \  
rm -Rf /usr/share/nginx/html/ && \  
# add www-data to root group (openshift requirement)  
adduser www-data root && \  
# for convenience  
ln -s /bin/bash /bin/ash && \  
touch /var/log/nginx/access.log && \  
touch /var/log/nginx/error.log && \  
mkdir /var/www && \  
# chmod conf dir so www-data can write to  
chown -R www-data:root /var/www/ /etc/nginx/ /usr/local/bin/run.sh
/var/log/nginx/ /var/run/ /var/cache/nginx/ && \  
chmod -R go+rwx /var/www/ /etc/nginx/ /usr/local/bin/run.sh /var/log/nginx/
/var/run/ /var/cache/nginx/ && \  
chmod +x /usr/local/bin/run.sh && \  
chmod +x /tini  
  
USER www-data  
  
EXPOSE 9080 9443  
ENTRYPOINT ["/tini", "--"]  
CMD ["/usr/local/bin/run.sh", "nginx", "-g", "daemon off;"]  

