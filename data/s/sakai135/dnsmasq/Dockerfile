FROM alpine:edge  
  
RUN apk add --update dnsmasq  
  
EXPOSE 53 53/udp  
  
ENTRYPOINT ["dnsmasq", "--no-hosts", "--no-daemon", "--keep-in-foreground", "
--log-queries"]  

