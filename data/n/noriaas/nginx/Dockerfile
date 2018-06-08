################################################################################  
# Base image  
################################################################################  
  
FROM nginx:stable-alpine  
  
################################################################################  
# Build instructions  
################################################################################  
  
ENV DEFAULT_UPLOAD_MAX_SIZE="32M" \  
DEFAULT_NGINX_MAX_WORKER_PROCESSES=2 \  
DEFAULT_APP_USER=noria \  
DEFAULT_APP_GROUP=noria \  
DEFAULT_APP_UID=1000 \  
DEFAULT_APP_GID=1000  
  
RUN apk add --no-cache --virtual .nginx-rundeps openssl bash \  
&& mkdir /etc/nginx/server.d \  
&& mkdir /etc/nginx/sites \  
&& mkdir /etc/nginx/sites-disabled \  
&& mkdir /etc/nginx/upstream \  
&& mkdir /etc/nginx/location \  
&& mkdir /etc/nginx/ssl  
  
# Add configuration files  
  
ADD docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
ADD nginx.conf /etc/nginx/  
COPY ./sites /etc/nginx/sites/  
COPY ./conf /etc/nginx/conf.d/  
COPY ./server.d /etc/nginx/server.d/  
COPY ./upstream /etc/nginx/upstream/  
  
STOPSIGNAL SIGTERM  
  
CMD ["/docker-entrypoint.sh"]

