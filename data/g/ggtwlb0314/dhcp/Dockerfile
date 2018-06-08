FROM ubuntu:14.04  
RUN apt-get update \  
&& apt-get install isc-dhcp-server  
  
ADD dhcpd.conf /etc/dhcp/  
  
EXPOSE 67/tcp 67/udp  
  
CMD /usr/sbin/dhcpd -user dhcpd -group dhcpd -f -4 -pf /tmp/dhcpd.pid -cf
/etc/dhcp/dhcpd.conf  

