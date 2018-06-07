FROM haproxy:alpine  
RUN addgroup -S haproxy && adduser -S -g haproxy haproxy  
VOLUME /var/lib/haproxy  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["haproxy", "-f", "/usr/local/etc/haproxy/haproxy.cfg"]

