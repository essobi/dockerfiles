FROM nginx  
  
MAINTAINER support@coscale.com  
  
LABEL
com.coscale.monitoring='[{"PluginType":"NGINX","Configuration":{"FILE":["\"/var/log/nginx/coscale-
access.log\" \"$server_name \"$request\" $request_time $status $request_length
$bytes_sent\""],"STATS URL":["http://localhost:8000/nginx_status"],"URL
CHECK":["http://localhost"]}}]'  
  
COPY coscale.conf /etc/nginx/conf.d/  

