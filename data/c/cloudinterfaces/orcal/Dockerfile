from alpine  
  
cmd ["/sbin/init"]  
  
run apk update && apk add openrc rsyslog dcron logrotate && \  
/sbin/rc-update add dcron && \  
/sbin/rc-update add rsyslog && \  
echo 'rc_controller_cgroups="NO"' >>/etc/rc.conf && \  
echo 'rc_sys="lxc"' >>/etc/rc.conf && \  
rm -rf /lib/rc/sh/rc-cgroup.sh && \  
echo 'rc_provide="loopback net"' >> /etc/rc.conf && \  
echo -e '::sysinit:/sbin/openrc sysinit\n::sysinit:/sbin/openrc default\n'
>/etc/inittab  
  
  
  

