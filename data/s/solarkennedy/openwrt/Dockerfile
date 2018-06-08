# WARNING  
# This doesn't work yet due to https://github.com/dotcloud/docker/issues/611  
FROM scratch  
MAINTAINER Kyle Anderson <kyle@xkyle.com>  
  
# We add our static binary because we can't use the 32 bit ones from openwrt  
# We also can't fetch it from the web directly, as the permissions would be
wrong  
ADD busybox-x86_64 /busybox-x86_64  
  
# Fetch an Openwrt Snapshot  
RUN ["/busybox-x86_64", "wget",
"http://downloads.openwrt.org/attitude_adjustment/12.09/x86/generic/openwrt-x86-generic-
rootfs.tar.gz" ]  
RUN ["/busybox-x86_64", "gunzip", "openwrt-x86-generic-rootfs.tar.gz" ]  
RUN ["/busybox-x86_64", "tar", "-x", "--exclude=./etc/resolv.conf", "--
exclude=./etc/hosts", "-f", "openwrt-x86-generic-rootfs.tar" ]  
  
# From here we have to use the static version of busybox, since our libraries
are all messed up  
RUN ["/busybox-x86_64", "rm", "openwrt-x86-generic-rootfs.tar"]  
  
# Convert the default networking in openwrt to be static for the one interface  
ADD network /etc/config/network  
ADD system /etc/config/system  
ADD inittab /etc/inittab  
  
# These end up setting kernel things we can't really set in docker  
RUN ["/busybox-x86_64", "rm", "/etc/rc.d/S45firewall"]  
RUN ["/busybox-x86_64", "rm", "/etc/rc.d/S05luci_fixtime"]  
RUN ["/busybox-x86_64", "rm", "/etc/rc.d/S60dnsmasq"]  
RUN ["/busybox-x86_64", "rm", "/etc/rc.d/S99sysctl"]  
RUN ["/busybox-x86_64", "rm", "/etc/rc.d/S98sysntpd"]  
  
USER root  
CMD /sbin/init  

