  
# see: https://github.com/andyshinn/docker-dnsmasq/tree/master  
FROM alpine:3.4  
RUN apk --no-cache add bash dnsmasq  
EXPOSE 53 53/udp  
  
COPY docker/entrypoint.sh /entrypoint.sh  
COPY docker/bin/hostadd /bin/hostadd  
COPY docker/bin/hostdel /bin/hostdel  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["dnsmasq", "-k"]  

