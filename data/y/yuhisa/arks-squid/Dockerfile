FROM alpine:3.4  
  
MAINTAINER "yuhisa-jp"  
  
ENV SQUID_USERNAME squid  
ENV SQUID_PASSWORD squid  
  
RUN apk --no-cache add squid apache2-utils && \  
rm -rf /var/cache/apk/*  
  
RUN sed -i 's/http_access allow localhost manager/http_access deny localhost
manager/g' /etc/squid/squid.conf && \  
sed -i 's/http_access allow localhost/http_access deny localhost/g'
/etc/squid/squid.conf && \  
sed -i 's/http_access allow localnet/http_access deny localnet/g'
/etc/squid/squid.conf && \  
sed -i 's/http_access deny all/#http_access deny all/g' /etc/squid/squid.conf
&& \  
sed -i 's/http_port 3128/#http_port 3128/g' /etc/squid/squid.conf && \  
echo "http_port 8080" >> /etc/squid/squid.conf && \  
echo "auth_param digest program /usr/lib/squid/digest_file_auth
/etc/squid/passwd" >> /etc/squid/squid.conf && \  
echo "auth_param digest children 8 startup=8 idle=8" >> /etc/squid/squid.conf
&& \  
echo "auth_param digest realm proxy" >> /etc/squid/squid.conf && \  
echo "auth_param digest nonce_garbage_interval 5 minutes" >>
/etc/squid/squid.conf && \  
echo "auth_param digest nonce_max_duration 30 minutes" >>
/etc/squid/squid.conf && \  
echo "auth_param digest nonce_max_count 50" >> /etc/squid/squid.conf && \  
echo "acl pauth proxy_auth REQUIRED" >> /etc/squid/squid.conf && \  
echo "http_access allow pauth" >> /etc/squid/squid.conf && \  
echo "cache_dir null /dev/null" >> /etc/squid/squid.conf && \  
echo "no_cache deny all" >> /etc/squid/squid.conf && \  
echo "cache_mem 64 MB" >> /etc/squid/squid.conf  
  
COPY start.sh /tmp/start.sh  
RUN chmod +x /tmp/start.sh  
  
EXPOSE 8080  
  
ENTRYPOINT ["/tmp/start.sh"]  

