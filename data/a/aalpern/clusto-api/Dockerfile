from debian:jessie  
  
# nginx  
run apt-get -y update  
run apt-get -y install curl  
run curl http://nginx.org/keys/nginx_signing.key | apt-key add -  
run echo 'deb http://nginx.org/packages/debian/ jessie nginx' >>
/etc/apt/sources.list  
run echo 'deb-src http://nginx.org/packages/debian/ jessie nginx' >>
/etc/apt/sources.list  
run apt-get -y update  
run apt-get -y install nginx-light  
  
# python stuff  
run apt-get -y install python-pip gunicorn supervisor  
  
# clusto  
run pip install clusto  
run pip install clusto-apiserver  
run pip install bottle  
  
add ./nginx.conf /etc/nginx/nginx.conf  
add ./clusto.conf /etc/clusto/clusto.conf  
add ./clusto.db /var/lib/clusto/clusto.db  
add ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Proxied clusto-apiserver with CORS headers  
expose :80  
# Direct clusto-apiserver  
expose :9664  
cmd ["/usr/bin/supervisord"]  

