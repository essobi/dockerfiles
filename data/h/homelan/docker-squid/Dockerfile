FROM alpine:3.6  
MAINTAINER olaf@home.lan  
  
ENV SQUID_CACHE_DIR=/var/cache/squid  
  
RUN set -ex \  
&& apk add --no-cache squid  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod u+x /docker-entrypoint.sh  
  
VOLUME ["${SQUID_CACHE_DIR}"]  
  
EXPOSE 3128/tcp  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/usr/sbin/squid", "-NYCd", "1", "-f", "/etc/squid/squid.conf"]  
  

