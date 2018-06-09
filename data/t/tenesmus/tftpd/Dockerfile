FROM alpine  
MAINTAINER Nathan Douglas <docker@tenesm.us>  
RUN set -xe \  
&& apk add --no-cache --virtual tmp_stuff \  
syslinux \  
gcc \  
binutils \  
make \  
perl \  
libc-dev \  
xz-dev \  
git \  
&& cp -r /usr/share/syslinux /tftp \  
&& git clone git://git.ipxe.org/ipxe.git \  
&& cd ipxe/src \  
&& make bin/ipxe.lkrn \  
&& cp bin/ipxe.lkrn /tftp/ \  
&& cd / \  
&& rm -rf /ipxe \  
&& apk del tmp_stuff \  
&& apk add --no-cache tftp-hpa \  
&& adduser -D tftp \  
&& mkdir -p /tftp/pxelinux.cfg \  
&& find /tftp -type f -exec chmod 0444 {} + \  
&& chmod 0777 /tftp/pxelinux.cfg  
EXPOSE 69/udp  
VOLUME /tftp/pxelinux.cfg  
ENTRYPOINT ["/usr/sbin/in.tftpd"]  
CMD ["-L","-u","tftp","--secure","/tftp","--verbose"]  

