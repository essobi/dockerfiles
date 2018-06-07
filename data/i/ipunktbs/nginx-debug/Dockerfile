FROM ipunktbs/nginx:1.10.2-7-1.4.0  
RUN apt-get update && apt-get -y install php7.0-xdebug \  
&& rm -Rf /var/lib/apt/lists \  
&& mkdir -p /opt/profiling ; chmod 777 /opt/profiling  
COPY 30-xdebug.ini /etc/php/7.0/fpm/conf.d/  
COPY 99-profiling.conf /etc/nginx/conf.d/  

