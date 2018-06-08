FROM alpine:3.4  
MAINTAINER Wei Gao<wei@gaofamily.org>  
  
RUN apk add --no-cache squid \  
&& sed -i -e 's/#http_access deny to_localhost/http_access deny to_localhost/'
/etc/squid/squid.conf \  
# && sed -i -e 's/http_port 3128/http_port 3128\nhttp_port 3129 intercept/'
/etc/squid/squid.conf \  
&& sed -i -e 's/#cache_dir ufs \/var\/cache\/squid 100 16 256/cache_dir ufs
\/var\/cache\/squid 1000 16 256/' /etc/squid/squid.conf \  
&& echo "access_log none" >> /etc/squid/squid.conf \  
&& echo "cache_store_log none" >> /etc/squid/squid.conf \  
&& echo "cache_log /dev/null" >> /etc/squid/squid.conf  
# && ln -snf /dev/stdout /var/log/squid/access.log \  
# && ln -snf /dev/stderr /var/log/squid/cache.log  
ADD docker-entrypoint.sh /  
  
EXPOSE 3128/tcp  
VOLUME ["/var/cache/squid"]  
  
ENTRYPOINT "/docker-entrypoint.sh"  

