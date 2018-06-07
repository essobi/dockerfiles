FROM alpine:edge  
  
RUN apk add -U iptables && rm -rf /var/cache/apk/*  
  
RUN chmod 4755 /sbin/xtables-multi  
  
ADD run.sh /run.sh  
  
ENTRYPOINT ["/run.sh"]  
  
USER nobody  

