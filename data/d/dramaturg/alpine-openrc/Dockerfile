  
FROM alpine  
MAINTAINER Sebastian Krohn <seb@gaia.sunn.de>  
  
ADD https://raw.githubusercontent.com/tests-always-included/mo/master/mo
/bin/mo  
RUN apk upgrade --update && \  
apk add openrc dcron bash && \  
rc-update add dcron default && \  
echo 'null::respawn:/sbin/syslogd -n -S -D -O /proc/1/fd/1' >> /etc/inittab &&
\  
rm -fr /tmp/* /var/cache/apk/* && \  
chmod +x /bin/mo  
  
# many thanks to github.com/neeravkumar/dockerfiles  
WORKDIR /etc/init.d  
RUN sed -i '/tty/d' /etc/inittab && \  
sed -i 's/#rc_sys=""/rc_sys="docker"/g' /etc/rc.conf && \  
echo 'rc_provide="loopback net"' >> /etc/rc.conf && \  
sed -i 's/^#\\(rc_logger="YES"\\)$/\1/' /etc/rc.conf && \  
sed -i 's/hostname $opts/# hostname $opts/g' /etc/init.d/hostname && \  
sed -i 's/mount -t tmpfs/# mount -t tmpfs/g' /lib/rc/sh/init.sh && \  
sed -i 's/cgroup_add_service /# cgroup_add_service /g' /lib/rc/sh/openrc-
run.sh && \  
rm -f hwclock hwdrivers modules modules-load modloop  
  
CMD ["/sbin/init"]  
  

