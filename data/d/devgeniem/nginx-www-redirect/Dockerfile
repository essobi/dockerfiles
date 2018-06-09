FROM nginx:stable-alpine  
MAINTAINER Onni Hakala <onni.hakala@geniem.com>  
  
# Install envsubst  
RUN \  
# Install envsubst command for replacing config files in system startup  
# - it needs libintl package  
# - only weights 100KB combined with it's libraries  
apk add \--no-cache bash gettext libintl \  
&& mv /usr/bin/envsubst /usr/local/bin/envsubst \  
&& apk del gettext  
  
# Add entrypoint which replaces nginx.conf  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
# Minimal nginx redirect config  
COPY nginx.conf.tmpl /etc/nginx/nginx.conf.tmpl  
  
# In order to log client IP-addresses we need to set real client ip from
X-Forwarded-For header.  
# In order to do that we need to know the public address and use it in the
NGINX_TRUSETD_IP env.  
env NGINX_PORT=80 \  
NGINX_TRUSTED_IP=127.0.0.1  
# Replace nginx config on startup  
ENTRYPOINT ["/docker-entrypoint.sh"]  

