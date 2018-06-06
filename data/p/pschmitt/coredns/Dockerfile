FROM alpine:3.6  
  
MAINTAINER Philipp Schmitt <philipp@schmitt.co>  
  
RUN apk add --no-cache --virtual deps curl && \  
apk add --no-cache ca-certificates openssl && \  
update-ca-certificates && \  
curl -L -o /tmp/coredns-latest.tgz \  
"$(curl -Ls https://api.github.com/repos/coredns/coredns/releases | \  
awk '/browser_download_url/ {print $2}' | sort -ru | \  
awk '/linux/ {print; exit}' | sed -r 's/"(.*)"/\1/')" && \  
tar -C /usr/bin -xvzf /tmp/coredns-latest.tgz && \  
adduser -h /config -S coredns && \  
rm /tmp/coredns-latest.tgz && \  
apk del deps  
  
USER coredns  
VOLUME ["/config"]  
EXPOSE 5353/udp  
  
ENTRYPOINT ["/usr/bin/coredns"]  
CMD ["-conf", "/config/Corefile"]  

