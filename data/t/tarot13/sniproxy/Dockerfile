FROM alpine  
  
LABEL maintainer "Ian Li <OpenSource@ianli.xyz>"  
  
RUN apk add --no-cache sniproxy  
  
ENTRYPOINT ["/usr/sbin/sniproxy"]  
  
CMD ["-c", "/etc/sniproxy/sniproxy.conf", "-f"]

