FROM gliderlabs/alpine:3.3  
MAINTAINER Oleg Fedoseev <oleg.fedoseev@me.com>  
  
RUN apk-install openrc openssh && ssh-keygen -A && \  
sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config && \  
echo 'root:docker.io' | chpasswd && \  
rc-update add sshd  
  
# patch openrc to work inside docker  
RUN sed -i 's/#rc_sys=""/rc_sys="docker"/g' /etc/rc.conf && \  
sed -i '/tty/d' /etc/inittab && \  
sed -i 's/hostname $opts/# hostname $opts/g' /etc/init.d/hostname && \  
sed -i 's/mount -t tmpfs/# mount -t tmpfs/g' /lib/rc/sh/init.sh && \  
sed -i 's/cgroup_add_service /# cgroup_add_service /g' /lib/rc/sh/openrc-
run.sh && \  
echo 'rc_provide="loopback net"' >> /etc/rc.conf  
  
EXPOSE 22  
CMD ["/sbin/init"]  

