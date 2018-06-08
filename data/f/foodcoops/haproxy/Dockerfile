FROM haproxy:1.7-alpine  
  
COPY docker-entrypoint2.sh reload-haproxy.sh /  
ENTRYPOINT ["/docker-entrypoint2.sh"]  
CMD ["haproxy", "-f", "/usr/local/etc/haproxy/haproxy.cfg"]  

