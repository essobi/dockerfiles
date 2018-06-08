FROM debian:stretch as qemu  
ARG QEMU_VER=2.11.1  
COPY sources.list /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get -y build-dep qemu  
RUN apt-get -y install ca-certificates git wget  
RUN git clone https://git.qemu.org/git/qemu.git  
WORKDIR /qemu  
RUN git checkout "tags/v$QEMU_VER" -b "stable-$QEMU_VER"  
RUN wget -O- https://github.com/resin-
io/qemu/commit/5851cf671e9d9dbfaa0127d31c2ef6d2833db875.diff | patch -p1  
RUN wget -O- https://github.com/resin-
io/qemu/commit/4406381ba21e5488d3f11d8868bd5b8ff1b82bed.diff | patch -p1  
RUN ./configure \  
\--target-list=mips-linux-user \  
\--static \  
\--disable-bluez \  
\--disable-capstone \  
\--disable-curses \  
\--disable-gcrypt \  
\--disable-kvm \  
\--disable-libssh2 \  
\--disable-slirp \  
\--disable-smartcard \  
\--disable-system \  
\--disable-tools \  
\--disable-vde \  
\--disable-vnc \  
\--disable-werror  
RUN make  
RUN file mips-linux-user/qemu-mips  
  
FROM debian:stretch as bootstrap  
RUN apt-get update && \  
apt-get -y install debootstrap wget  
COPY \--from=qemu /qemu/mips-linux-user/qemu-mips /usr/bin/qemu-mips-static  
COPY \--from=qemu /qemu/mips-linux-user/qemu-mips /bootstrap/usr/bin/qemu-
mips-static  
RUN debootstrap --arch mips --foreign stretch /bootstrap  
RUN wget -O /bootstrap/bin/mount https://dl.lochnair.net/dummy.mips  
RUN chroot /bootstrap /usr/bin/qemu-mips-static -execve /bin/bash -c
'/debootstrap/debootstrap --second-stage'  
RUN mv -v /bootstrap/bin/sh /bootstrap/bin/sh.real  
COPY sh-shim /bootstrap/bin/sh  
COPY sh-shim /bootstrap/usr/bin/sh-shim  
  
FROM scratch  
COPY \--from=bootstrap /bootstrap/. /

