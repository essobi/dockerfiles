FROM ubuntu:14.10  
  
MAINTAINER Vincent Palmer <shift+gh@someone.section.me>  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update \  
&& apt-get -y install wget syslinux atftpd wget \  
&& apt-get autoremove \  
&& apt-get clean \  
&& rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* \  
&& mkdir -p /tftpboot/pxelinux.cfg \  
&& cp /usr/lib/syslinux/modules/efi64/menu.c32 /tftpboot \  
&& cd /tftpboot \  
&& wget http://alpha.release.core-
os.net/amd64-usr/current/coreos_production_pxe.vmlinuz \  
&& wget http://alpha.release.core-
os.net/amd64-usr/current/coreos_production_pxe_image.cpio.gz \  
&& echo "Used for testing" > validation  
  
CMD /usr/sbin/atftpd \--user nobody.nogroup \--daemon \--no-fork \--port 69
\--logfile /dev/stdout /tftpboot  

