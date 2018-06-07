FROM kinsamanka/docker-qemu-chroot  
MAINTAINER GP Orcullo <kinsamanka@gmail.com>  
  
# build armv7l rootfs under /opt  
RUN cd /opt && \  
debootstrap \--foreign \--no-check-gpg \--include=ca-certificates \  
\--arch=armhf wheezy rootfs http://httpredir.debian.org/debian && \  
proot -r /opt/rootfs -q qemu-arm-static \  
/debootstrap/debootstrap \--second-stage \--verbose  
# configure and cleanup apt  
RUN sh -c 'echo "deb http://httpredir.debian.org/debian wheezy main" \  
> /opt/rootfs/etc/apt/sources.list' && \  
sh -c 'echo "deb http://httpredir.debian.org/debian wheezy-updates main" \  
>> /opt/rootfs/etc/apt/sources.list' && \  
sh -c 'echo "deb http://security.debian.org wheezy/updates main" \  
>> /opt/rootfs/etc/apt/sources.list' && \  
proot -r /opt/rootfs -q qemu-arm-static apt-get clean  
  
# fix resolv.conf  
RUN sh -c 'echo "nameserver 8.8.8.8" > /opt/rootfs/etc/resolv.conf' && \  
sh -c 'echo "nameserver 8.8.4.4" >>/opt/rootfs/etc/resolv.conf'  
  

