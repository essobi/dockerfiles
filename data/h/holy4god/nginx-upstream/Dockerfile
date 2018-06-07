FROM nginx:alpine  
ENV UPSTREAM_HOST 127.0.0.1  
ENV UPSTREAM_PORT 9090  
COPY default.conf.tpl /etc/nginx/conf.d/default.conf.tpl  
  
CMD envsubst '${UPSTREAM_HOST} ${UPSTREAM_PORT}' <
/etc/nginx/conf.d/default.conf.tpl > /etc/nginx/conf.d/default.conf && nginx
-g 'daemon off;'

