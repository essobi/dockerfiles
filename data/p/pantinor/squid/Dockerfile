FROM alpine:3.3  
MAINTAINER paolo.antinori@gmail.com  
RUN apk update \  
&& apk add squid \  
&& apk add acl \  
&& rm -rf /var/cache/apk/*  
RUN printf "cache_dir aufs /var/cache/squid3 5000 16 16\nmaximum_object_size
2048 MB" >> /etc/squid/squid.conf  
  
COPY start-squid.sh /usr/local/bin/  
  
CMD ["/usr/local/bin/start-squid.sh"]  

