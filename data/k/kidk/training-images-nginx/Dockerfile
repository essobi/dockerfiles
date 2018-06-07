FROM richarvey/nginx-php-fpm  
  
MAINTAINER Samuel Vandamme <samuel.vandamme@coscale.com>  
  
ENV RECEIVER_HOST receiver  
  
COPY src/ /var/www/html/  
  
COPY nginx.conf /etc/nginx/  
  
LABEL
com.coscale.monitoring='[{"PluginType":"NGINX","Configuration":{"FILE":["\"/var/log/nginx/coscale-
access.log\" \"$server_name \"$request\" $request_time $status $request_length
$bytes_sent\""],"STATS URL":["http://localhost:8000/nginx_status"],"URL
CHECK":["http://localhost"]}}]'

