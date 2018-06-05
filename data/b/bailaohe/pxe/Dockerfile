FROM debian  
MAINTAINER He Bai <bai.he@outlook.com>  
  
ENV ARCH amd64  
ENV DIST jessie  
ENV MIRROR http://ftp.nl.debian.org  
  
RUN apt-get -q update  
RUN apt-get -qy install dnsmasq wget iptables  
RUN wget --no-check-certificate
https://raw.github.com/jpetazzo/pipework/master/pipework  
RUN chmod +x pipework  
RUN mkdir /tftp  
WORKDIR /tftp  
  
RUN wget
$MIRROR/debian/dists/$DIST/main/installer-$ARCH/current/images/netboot/debian-
installer/$ARCH/linux  
RUN wget
$MIRROR/debian/dists/$DIST/main/installer-$ARCH/current/images/netboot/debian-
installer/$ARCH/initrd.gz  
RUN wget
$MIRROR/debian/dists/$DIST/main/installer-$ARCH/current/images/netboot/debian-
installer/$ARCH/pxelinux.0  
RUN mkdir pxelinux.cfg  
RUN printf "DEFAULT linux\nKERNEL linux\nAPPEND initrd=initrd.gz\n"
>pxelinux.cfg/default  
  
CMD \  
if [ -z "$DHCP_RANGE" ]; then echo "DHCP_RANGE is not set!"; exit 1; fi &&\  
if [ -z "$BOOT_SERVER" ]; then echo "BOOT_SERVER is not set!"; exit 1; fi &&\  
echo Setting up iptables... &&\  
iptables -t nat -A POSTROUTING -j MASQUERADE &&\  
echo Waiting for pipework to give us the eth1 interface... &&\  
/pipework --wait &&\  
echo Starting DHCP+TFTP server...&&\  
dnsmasq --interface=eth1 \  
\--dhcp-range=$DHCP_RANGE,1h \  
\--dhcp-boot=pxelinux.0,pxeserver,$BOOT_SERVER \  
\--pxe-service=x86PC,"Install Debian ${DIST}",pxelinux \  
\--enable-tftp --tftp-root=/tftp/ --no-daemon  
  

