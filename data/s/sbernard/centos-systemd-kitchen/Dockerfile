FROM sbernard/centos-chef  
MAINTAINER Samuel Bernard "samuel.bernard@gmail.com"  
# Let's run stuff  
RUN \  
# Mask remount-fs as it will always fail in a docker  
systemctl mask systemd-remount-fs.service sys-fs-fuse-connections.mount  
  
VOLUME ["/sys/fs/cgroup", "/run"]  
CMD ["/usr/lib/systemd/systemd"]  

