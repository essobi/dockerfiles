# https://wiki.alpinelinux.org/wiki/Setting_up_unbound_DNS_server  
FROM alpine  
EXPOSE 53/udp  
RUN apk add --no-cache unbound wget && \  
wget -S https://www.internic.net/domain/named.cache -O /etc/unbound/root.hints  
COPY ./unbound.conf /etc/unbound/  
ENTRYPOINT ["unbound", "-d"]  

