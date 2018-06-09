FROM alpine  
  
MAINTAINER StevenACoffman <steve.coffman@ithaka.org>  
RUN apk add --update bash && apk add jq && apk add --update curl && apk add
--no-cache util-linux && rm -rf /var/cache/apk/*  
ADD eureka-kube-sidecar.sh /opt/  
  
ENTRYPOINT ["/opt/eureka-kube-sidecar.sh"]  

