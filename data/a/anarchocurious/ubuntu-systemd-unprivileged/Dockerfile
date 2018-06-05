FROM ubuntu:16.04  
MAINTAINER "Alec Larsen" <alec.larsen@agapered.com>  
  
RUN systemctl mask -- \  
-.mount \  
dev-mqueue.mount \  
dev-hugepages.mount \  
etc-hosts.mount \  
etc-hostname.mount \  
etc-resolv.conf.mount \  
proc-bus.mount \  
proc-irq.mount \  
proc-kcore.mount \  
proc-sched_debug.mount \  
proc-sys-fs-binfmt_misc.mount \  
proc-sys-fs-binfmt_misc.automount \  
proc-fs.mount \  
'proc-sysrq\x2dtrigger.mount' \  
proc-timer_list.mount \  
sys-fs-fuse-connections.mount \  
sys-kernel-config.mount \  
sys-kernel-debug.mount \  
tmp.mount \  
console-getty.service \  
display-manager.service \  
getty-static.service \  
getty@tty1.service \  
hwclock-save.service \  
systemd-logind.service \  
ondemand.service \  
systemd-remount-fs.service \  
systemd-tmpfiles-setup.service \  
systemd-sysctl.service \  
systemd-modules-load.service \  
systemd-machine-id-commit.service \  
systemd-ask-password-console.path \  
systemd-ask-password-wall.path \  
swap.target \  
&& \  
systemctl set-default multi-user.target \  
&& \  
find /etc/systemd/system -type l -name '*.service' -! -exec test -e {} \;
-delete  
  
ENV container docker  
STOPSIGNAL 37  
VOLUME ["/sys/fs/cgroup", "/run", "/run/lock"]  
CMD ["/sbin/init"]  
  

