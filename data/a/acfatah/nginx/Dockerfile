FROM alpine:3.5  
  
ARG nginx_access_log_path=/var/log/nginx/log  
ARG nginx_access_log_file=access.log  
ARG nginx_access_log_format=main  
ARG nginx_client_max_body_size=1m  
ARG nginx_error_log_path=/var/log/nginx/log  
ARG nginx_error_log_file=error.log  
ARG nginx_error_log_level=warn  
ARG nginx_keepalive_timeout=65  
ARG nginx_root=/var/www/localhost/htdocs  
ARG nginx_server_name=localhost  
ARG nginx_server_tokens=off  
ARG nginx_worker_connections=1024  
ARG nginx_worker_processes=auto  
  
RUN apk update && \  
apk upgrade && \  
addgroup -S nginx && \  
adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx && \  
apk add nginx && \  
rm -frv /var/cache/apk/*  
  
COPY ./nginx.conf.tpl /etc/nginx/nginx.conf  
COPY ./conf/default.conf.tpl /etc/nginx/conf.d/default.conf  
  
RUN \  
# /etc/nginx/nginx.conf  
sed -i "s|{{nginx_worker_processes}}|${nginx_worker_processes}|g"
/etc/nginx/nginx.conf && \  
sed -i "s|{{nginx_error_log_path}}|${nginx_error_log_path}|g"
/etc/nginx/nginx.conf && \  
sed -i "s|{{nginx_error_log_file}}|${nginx_error_log_file}|g"
/etc/nginx/nginx.conf && \  
sed -i "s|{{nginx_error_log_level}}|${nginx_error_log_level}|g"
/etc/nginx/nginx.conf && \  
sed -i "s|{{nginx_worker_connections}}|${nginx_worker_connections}|g"
/etc/nginx/nginx.conf && \  
sed -i "s|{{nginx_server_tokens}}|${nginx_server_tokens}|g"
/etc/nginx/nginx.conf && \  
sed -i "s|{{nginx_error_log_level}}|${nginx_error_log_level}|g"
/etc/nginx/nginx.conf && \  
sed -i "s|{{nginx_client_max_body_size}}|${nginx_client_max_body_size}|g"
/etc/nginx/nginx.conf && \  
sed -i "s|{{nginx_keepalive_timeout}}|${nginx_keepalive_timeout}|g"
/etc/nginx/nginx.conf && \  
sed -i "s|{{nginx_access_log_path}}|${nginx_access_log_path}|g"
/etc/nginx/nginx.conf && \  
sed -i "s|{{nginx_access_log_file}}|${nginx_access_log_file}|g"
/etc/nginx/nginx.conf && \  
sed -i "s|{{nginx_access_log_format}}|${nginx_access_log_format}|g"
/etc/nginx/nginx.conf && \  
\  
# /etc/nginx/conf.d/default.conf  
sed -i "s|{{nginx_server_name}}|${nginx_server_name}|g"
/etc/nginx/conf.d/default.conf && \  
sed -i "s|{{nginx_root}}|${nginx_root}|g" /etc/nginx/conf.d/default.conf && \  
\  
# forward request and error logs to docker log collector  
mkdir -p ${nginx_access_log_path} && touch ${nginx_access_log_file} && \  
mkdir -p ${nginx_error_log_path} && touch ${nginx_error_log_file} && \  
ln -sf /dev/stdout ${nginx_access_log_path}/${nginx_access_log_file} && \  
ln -sf /dev/stderr ${nginx_error_log_path}/${nginx_error_log_file} && \  
\  
# Fix https://github.com/gliderlabs/docker-alpine/issues/185  
mkdir -p /run/nginx  
  
EXPOSE 80 443  
  
CMD ["nginx", "-g", "daemon off;"]  

