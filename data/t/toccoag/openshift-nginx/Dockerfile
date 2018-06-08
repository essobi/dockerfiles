from nginx:latest  
ADD nice2.conf /etc/nginx/conf.d/  
ADD nginx.conf /etc/nginx/  
ADD header_config.py /usr/local/bin/  
ADD entrypoint /usr/local/bin/  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends python3 \  
&& rm -r /var/cache/apt/* \  
&& chmod -R 777 /var/log/nginx /var/cache/nginx /var/run \  
&& chgrp -R 0 /etc/nginx \  
&& chmod -R g+rwX /etc/nginx \  
&& rm -f /etc/nginx/conf.d/default.conf \  
&& chmod +x /usr/local/bin/header_config.py /usr/local/bin/entrypoint  
EXPOSE 8081  
ENTRYPOINT ["/usr/local/bin/entrypoint"]  

