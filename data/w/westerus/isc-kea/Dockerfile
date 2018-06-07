FROM westerus/isc-kea:base  
MAINTAINER Westerus <westerus@gmail.com>  
  
LABEL manteiner="Westerus <westerus@gmail.com>" \  
description="ISC Kea DHCPv6 Service" \  
version="0.1.0"  
  
COPY /rootfs/entry-point.sh /  
  
WORKDIR /root  
  
ENTRYPOINT ["/entry-point.sh"]  
CMD ["kea-dhcp6","-d","-c","$KEACONF"]  

