FROM colstrom/alpine  
RUN apk-install squid  
ADD squid.sh /usr/local/bin/squid  
RUN sed -i 's/^#cache_dir/cache_dir/' /etc/squid/squid.conf \  
&& echo 'cache_log /var/log/squid/cache.log' | tee -a /etc/squid/squid.conf \  
&& echo 'access_log daemon:/var/log/squid/access.log' | tee -a
/etc/squid/squid.conf \  
&& chmod a+x /usr/local/bin/squid  
  
EXPOSE 3128  
VOLUME ["/etc/squid", "/var/cache/squid", "/var/log/squid"]  
  
ENTRYPOINT ["squid"]  

