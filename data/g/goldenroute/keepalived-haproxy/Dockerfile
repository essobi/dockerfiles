FROM haproxy:1.7.3  
ENV KEEPALIVED_VERSION 1:1.2.13-1  
RUN apt-get update && \  
apt-get install --no-install-recommends --no-install-suggests -y
keepalived=${KEEPALIVED_VERSION} && \  
rm -rf /var/lib/apt/lists/*  
  
COPY docker-entrypoint-override.sh /  
COPY keepalived /keepalived/  
  
RUN chmod +x /docker-entrypoint-override.sh  
RUN chmod +x /keepalived/*.sh  
  
ENTRYPOINT ["/docker-entrypoint-override.sh"]  
  
CMD ["haproxy", "-f", "/usr/local/etc/haproxy/haproxy.cfg"]

