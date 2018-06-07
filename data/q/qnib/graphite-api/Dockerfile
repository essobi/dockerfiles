###### pure graphite-api  
FROM qnib/alpn-rsyslog  
  
ADD etc/init.d/graphite-api /etc/init.d/  
RUN apk update && \  
# Graphite-API  
apk add py-pip libffi-dev gcc python-dev musl-dev cairo && \  
pip install graphite-api && \  
mkdir -p /var/lib/graphite && \  
# gunicorn & nginx  
apk add py-gunicorn nginx && \  
# Remove some stuff - should be even less  
apk del gcc libffi-dev binutils binutils-libs musl-dev python-dev && \  
rm -rf /var/cache/apk/*  
ADD etc/graphite-api.yaml /etc/graphite-api.yaml  
ADD etc/consul.d/graphite-api.json \  
etc/consul.d/nginx.json \  
/etc/consul.d/  
ADD etc/supervisord.d/graphite-api.ini \  
etc/supervisord.d/nginx.ini \  
/etc/supervisord.d/  
ADD etc/nginx/nginx.conf /etc/nginx/nginx.conf  
ADD etc/nginx/conf.d/graphite-api.conf /etc/nginx/conf.d/  

