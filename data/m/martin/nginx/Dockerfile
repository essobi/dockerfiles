FROM nginx:latest  
  
MAINTAINER Martin van Beurden <chadoe@gmail.com>  
  
ENV DATA_DIR /app/  
  
ADD start.sh /usr/local/bin/  
  
ONBUILD ADD app $DATA_DIR  
ONBUILD ADD conf /etc/nginx/conf.d/  
  
# Disable daemon mode  
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \  
# Defaults proxy_params  
echo 'proxy_connect_timeout 600;' >> /etc/nginx/proxy_params && \  
echo 'proxy_send_timeout 600;' >> /etc/nginx/proxy_params && \  
echo 'proxy_read_timeout 600;' >> /etc/nginx/proxy_params && \  
echo 'send_timeout 600;' >> /etc/nginx/proxy_params && \  
# Defaults fastcgi_params  
echo 'fastcgi_connect_timeout 60;' >> /etc/nginx/fastcgi_params && \  
echo 'fastcgi_send_timeout 150;' >> /etc/nginx/fastcgi_params && \  
echo 'fastcgi_read_timeout 300;' >> /etc/nginx/fastcgi_params && \  
# backup  
cp -a /etc/nginx/conf.d /etc/nginx/.conf.d.orig && \  
rm -f /etc/nginx/conf.d/default.conf && \  
mkdir -p $DATA_DIR && \  
chown -R www-data:www-data $DATA_DIR  
  
WORKDIR /etc/nginx  
  
CMD ["/usr/local/bin/start.sh"]  

