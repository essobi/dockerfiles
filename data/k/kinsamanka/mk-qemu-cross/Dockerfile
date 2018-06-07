FROM kinsamanka/docker-qemu-chroot:wheezy-base  
MAINTAINER GP Orcullo <kinsamanka@gmail.com>  
  
ADD configure_apt.sh /opt/rootfs/tmp/  
RUN proot -r /opt/rootfs -q qemu-arm-static /tmp/configure_apt.sh  
  
# install dependencies  
ADD install_dependencies.sh /opt/rootfs/tmp/  
RUN proot -r /opt/rootfs -q qemu-arm-static /tmp/install_dependencies.sh  
  
ADD arm-linux-gnueabihf-* /opt/rootfs/usr/bin/  
  
# default run command  
CMD proot -b /dev/shm -r /opt/rootfs -q qemu-arm-static /bin/bash  

