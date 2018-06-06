FROM crux:latest  
MAINTAINER Danny Rawlins <contact at romster dot me>  
  
VOLUME /var/cache/ccache  
VOLUME /var/ports/packages  
VOLUME /var/log/pkgbuild  
VOLUME /usr/ports  
  
ENV SHELL=/bin/sh  
  
ADD prt-get.conf pkgmk.conf profile /etc/  
  
ADD \  
http://crux.ster.zone/projects/crux/crux.asm \  
http://crux.ster.zone/projects/crux/Makefile \  
http://crux.ster.zone/projects/prt-ins/prt-ins-1.0.tar.xz \  
/tmp/  
  
# this reduces the time for ports -u  
ADD \  
http://crux.ster.zone/ports/core-3.1.tar.xz \  
http://crux.ster.zone/ports/opt-3.1.tar.xz \  
http://crux.ster.zone/ports/xorg-3.1.tar.xz \  
http://crux.ster.zone/ports/compat-32-3.1.tar.xz \  
http://crux.ster.zone/ports/contrib-3.1.tar.xz \  
http://crux.ster.zone/ports/xfce-3.1.tar.xz \  
http://crux.ster.zone/ports/kde4-3.0.tar.xz \  
http://crux.ster.zone/ports/enlightenment-3.0.tar.xz \  
http://crux.ster.zone/ports/romster-master.tar.xz \  
/usr/ports/  
  
#RUN \  
# cd /usr/ports/ && \  
# bsdtar -xvf core-3.1.tar.xz && \  
# bsdtar -xvf opt-3.1.tar.xz && \  
# bsdtar -xvf xorg-3.1.tar.xz && \  
# bsdtar -xvf compat-32-3.1.tar.xz && \  
# bsdtar -xvf contrib-3.1.tar.xz && \  
# bsdtar -xvf xfce-3.1.tar.xz && \  
# bsdtar -xvf kde4-3.0.tar.xz && \  
# bsdtar -xvf enlightenment-3.0.tar.xz && \  
# bsdtar -xvf romster-master.tar.xz  
ADD https://crux.nu/portdb/?a=getup&q=romster /etc/ports/romster.httpup  
ADD https://crux.nu/portdb/?a=getup&q=kde4 /etc/ports/kde4.rsync  
ADD https://crux.nu/portdb/?a=getup&q=xfce /etc/ports/xfce.rsync  
ADD https://crux.nu/portdb/?a=getup&q=enlightenment
/etc/ports/enlightenment.rsync  
  
# /usr/sbin/prt-ins  
RUN \  
cd /tmp && \  
bsdtar -xf prt-ins-1.0.tar.xz && \  
cd prt-ins-1.0 && \  
make && \  
make install && \  
make clean && \  
cd / && \  
rm /tmp/prt-ins-1.0/* && \  
rmdir /tmp/prt-ins-1.0  
  
# ASM version of /usr/bin/crux for speed with ccache  
RUN \  
cd /tmp && \  
make && \  
make install && \  
make clean && \  
rm /tmp/{crux.asm,Makefile} && \  
cd -  
  
RUN \  
prt-ins -i '/usr/ports/xorg' -p '/usr/ports/compat-32' && \  
prt-ins -i '/usr/ports/compat-32' -p '/usr/ports/contrib' && \  
prt-ins -i '/usr/ports/contrib' -p '/usr/ports/romster:pkg-not' && \  
prt-ins -i '/usr/ports/contrib' -p '/usr/ports/romster:pkg-url' && \  
prt-ins -i '/usr/ports/contrib' -p '/usr/ports/romster:check-32-versions' && \  
mkdir -p /var/ports/packages && \  
mv /etc/ports/contrib.rsync{.inactive,} && \  
mv /etc/ports/compat-32.rsync{.inactive,} && \  
ports -u && \  
prt-get depinst vim ccache kmod httpup elfutils prt-utils pkg-not pkg-url
check-32-versions && \  
prt-get remove elfutils && \  
prt-get sysup && \  
prtwash -a -s -p  
  
CMD . /etc/profile && /bin/sh  

