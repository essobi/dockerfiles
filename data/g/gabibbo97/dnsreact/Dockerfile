FROM alpine:latest  
  
LABEL maintainer="gabibbo97@gmail.com"  
  
RUN apk add --no-cache bind-tools ncurses  
RUN rm /usr/sbin/dnssec-* /usr/bin/host /usr/bin/nsupdate /usr/bin/nslookup
/usr/bin/delv  
  
ADD [ "./dnsreact.sh", "/" ]  
ADD [ "./dns_forall.sh", "/" ]  
ADD [ "./dns_foreach.sh", "/" ]  
ADD [ "./dns_onchange.sh", "/" ]  
  
ENTRYPOINT [ "./dnsreact.sh" ]

