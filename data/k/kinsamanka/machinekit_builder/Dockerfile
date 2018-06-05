FROM kinsamanka/machinekit_builder:base  
MAINTAINER GP Orcullo <kinsamanka@gmail.com>  
#  
# These variables configure the build.  
#  
ENV SUITE jessie  
ENV ARCH armhf  
#  
# [Leave surrounding comments to eliminate merge conflicts]  
#  
ENV PROOT_OPTS "-b /dev/urandom"  
# create chroot  
ADD wheezy.conf jessie.conf /  
RUN multistrap -f /${SUITE}.conf -a ${ARCH} -d ${ROOTFS} && \  
proot-helper /var/lib/dpkg/info/dash.preinst install && \  
proot-helper dpkg --configure -a  
  
ENV PROOT_OPTS "-b /dev/pts -b /dev/shm -b /dev/urandom"  
# fix resolv.conf  
RUN echo "nameserver 8.8.8.8\nnameserver 8.8.4.4" \  
> ${ROOTFS}/etc/resolv.conf  
  
# 3rd-party MK deps repo  
RUN proot-helper apt-key adv --keyserver hkp://keys.gnupg.net \  
\--recv-key 73571BB9 && \  
echo "deb http://deb.dovetail-automata.com ${SUITE} main" \  
> ${ROOTFS}/etc/apt/sources.list.d/machinekit.list  
# update apt db  
RUN proot-helper apt-get update  
  
# install MK dependencies  
ADD mk_depends ${ROOTFS}/tmp/  
# mk_depends lists deps independent of $SUITE and $ARCH  
RUN proot-helper xargs -a /tmp/mk_depends apt-get install -y  
RUN rm ${ROOTFS}/tmp/mk_depends  
  
# cython package is in backports on Wheezy  
RUN test $SUITE = wheezy \  
&& proot-helper apt-get install -y -t wheezy-backports cython \  
|| proot-helper apt-get install -y cython  
  
# tcl/tk latest is v. 8.5 in Wheezy  
RUN test $SUITE = wheezy \  
&& proot-helper apt-get install -y tcl8.5-dev tk8.5-dev \  
|| proot-helper apt-get install -y tcl8.6-dev tk8.6-dev  
  
# cleanup apt  
RUN proot-helper apt-get clean && \  
rm -f /var/lib/apt/lists/* ${ROOTFS}/var/lib/apt/lists/* || true  
  
# copy arm-linux-gnueabihf-* last to clobber package installs  
ADD bin/* ${ROOTFS}/tmp/  
  
# use modified arm-linux-gnueabihf-* if running on wheezy  
RUN test $ARCH = armhf && test $SUITE = wheezy \  
&& cp ${ROOTFS}/tmp/arm-* ${ROOTFS}/usr/bin/ \  
|| true  
  
# else use native arm-linux-gnueabihf-*  
RUN test $ARCH = armhf && test $SUITE = jessie \  
&& proot-helper sh -c '\  
for a in $(ls /host-rootfs/usr/bin/arm-linux-gnueabihf-*); \  
do \  
ln -sf $a /usr/bin; \  
done' \  
|| true  
  
# cleanup  
RUN rm ${ROOTFS}/tmp/*  
  
# update ccache symlinks  
RUN proot-helper dpkg-reconfigure ccache  

