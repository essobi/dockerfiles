FROM haproxy:alpine  
  
RUN apk add --no-cache bash  
  
COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg  
COPY haproxy-redis-lb-init.sh /usr/local/bin/haproxy-redis-lb-init.sh  
  
EXPOSE 6379  
ENTRYPOINT [ "/usr/local/bin/haproxy-redis-lb-init.sh" ]  
CMD ["haproxy", "-f", "/usr/local/etc/haproxy/haproxy.cfg"]

