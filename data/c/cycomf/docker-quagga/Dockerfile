# docker run --rm -ti --name isp_peering progrium/busybox /bin/sh  
FROM progrium/busybox  
  
ADD rc.common /etc/  
ADD service.sh /lib/functions/  
ADD pipework /usr/bin/  
ADD start_router /usr/bin/  
  
RUN echo "src/gz routing
http://downloads.openwrt.org/snapshots/trunk/x86_64/generic/packages/routing"
>> /etc/opkg.conf \  
&& adduser -D -H -S network network \  
&& opkg-install ip quagga quagga-bgpd quagga-vtysh quagga-zebra openvpn  
  
VOLUME /etc/quagga/  
  
CMD /usr/bin/start_router  

