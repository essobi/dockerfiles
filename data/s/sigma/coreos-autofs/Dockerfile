FROM debian:jessie  
MAINTAINER Yann Hodique <hodiquey@vmware.com>  
  
RUN apt-get update && apt-get install -y bison flex build-essential  
ADD . /src  
WORKDIR /src  
  
VOLUME /opt /etc/autofs /etc/systemd/system  
  
RUN ./configure \--prefix=/opt \--sysconfdir=/etc/autofs \  
\--with-systemd=/etc/systemd/system \  
MOUNT=/usr/bin/mount UMOUNT=/usr/bin/umount MOUNT_NFS=/usr/sbin/mount.nfs \  
MODPROBE=/usr/sbin/modprobe E2FSCK=/usr/sbin/fsck.ext2 \  
E3FSCK=/usr/sbin/fsck.ext3 E4FSCK=/usr/sbin/fsck.ext4  
RUN make  
  
ENTRYPOINT ["make", "install"]  

