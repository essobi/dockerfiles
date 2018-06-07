FROM khipu/base-alpine-s6  
MAINTAINER developers@khipu.com  
  
RUN apk add --update dnsmasq inotify-tools \  
&& rm -rf /var/cache/apk/*  
  
ADD services.d/hosts-watch.sh /etc/services.d/hosts-watch/run  
ADD services.d/dnsmasq.sh /etc/services.d/dnsmasq/run  
ENTRYPOINT ["/init"]  

