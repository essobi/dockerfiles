FROM hivesolutions/alpine:latest  
  
LABEL version="1.0"  
LABEL maintainer="Hive Solutions <development@hive.pt>"  
  
EXPOSE 67/udp  
  
ADD dhcpd.conf /etc/dhcp/config/dhcp/dhcpd.conf  
ADD hive.conf /etc/dhcp/config/dhcp/hive.conf  
  
WORKDIR /etc/dhcp  
  
RUN apk update && apk add dhcp  
RUN ln -s /etc/dhcp/config/dhcp/dhcpd.conf /etc/dhcp/dhcpd.conf  
RUN touch /var/lib/dhcp/dhcpd.leases  
  
CMD ["/usr/sbin/dhcpd", "-f", "-d", "-cf", "/etc/dhcp/dhcpd.conf"]  

