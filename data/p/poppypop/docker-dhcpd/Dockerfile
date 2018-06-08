FROM alpine:latest  
  
RUN set -xe \  
&& apk update --no-cache && apk upgrade --no-cache \  
&& apk add --no-cache --update --no-progress bash dhcp \  
&& rm -rf /var/cache/apk/*  
  
EXPOSE 67/tcp 67/udp  
EXPOSE 547/tcp 547/udp  
EXPOSE 647/tcp 647/udp  
EXPOSE 847/tcp 847/udp  
  
EXPOSE 7911/tcp 7911/udp  
  
RUN ["touch", "/var/lib/dhcp/dhcpd.leases"]  
  
VOLUME ["/data"]  
  
ENTRYPOINT ["dhcpd"]  
CMD ["-f", "-d", "-cf", "/data/dhcpd.conf", "-lf", "/data/dhcpd.leases", "--
no-pid"]  

