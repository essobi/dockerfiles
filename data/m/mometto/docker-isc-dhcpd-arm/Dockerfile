FROM resin/armv7hf-debian-qemu  
  
RUN [ "cross-build-start" ]  
  
RUN apt-get update \  
&& apt-get install -y isc-dhcp-server \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN touch /var/lib/dhcp/dhcpd.leases  
  
RUN [ "cross-build-end" ]  
  
VOLUME ["/var/lib/dhcp", "/etc/dhcp"]  
  
ENTRYPOINT ["/usr/sbin/dhcpd", "-d", "--no-pid"]  
  

