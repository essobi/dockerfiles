FROM alpine:latest  
MAINTAINER Craig Tracey <craigtracey@gmail.com>  
  
COPY docker-entrypoint.sh /bin/docker-entrypoint.sh  
RUN apk update && apk add dnsmasq syslinux inotify-tools  
RUN mkdir -p /var/lib/tftproot && ln -s /usr/share/syslinux
/var/lib/tftproot/pxelinux  
RUN wget http://boot.ipxe.org/undionly.kpxe -O /var/lib/tftproot/undionly.kpxe
&& md5sum /var/lib/tftproot/undionly.kpxe | [ `awk '{print $1}'` ==
"ec75a06c4c0b3615d77811bd991f41f3" ]  
RUN wget http://boot.ipxe.org/ipxe.pxe -O /var/lib/tftproot/ipxe.pxe && md5sum
/var/lib/tftproot/ipxe.pxe | [ `awk '{print $1}'` ==
"89c5036c2d705dd5e69ddf11a2c4d15f" ]  
  
CMD ["/bin/docker-entrypoint.sh"]  

