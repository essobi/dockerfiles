##################################  
###  
### This project starts from centos:7 build and installs systemd (container)
and latest docker  
###  
### - remount /sys/fs/cgroups within the context its launched into (side
effect of \--priv)  
### - launches docker (Working how to let SystemD do this  
### - passes control to SystemD (unless told to do otherwise)  
###  
### Ideas (and portions of code in the project) originated from  
### https://github.com/jpetazzo/dind  
### https://github.com/maci0/docker-systemd-unpriv  
###  
##################################  
  
FROM centos:centos7  
MAINTAINER Rick Alm "rickalm@aol.com"  
  
# Add our start scripts to the image  
#  
ADD files /  
  
# Set environment var container to docker  
#  
ENV container docker  
  
# Try to always use /entrypoint.sh as entrypoint to a container  
#  
ENTRYPOINT ["/entrypoint.sh"]  
  
# declare /run and /sys/fs as volumes so they are not tied to overlayfs and
therfore "remountable"  
#  
VOLUME [ "/run", "/sys/fs/cgroup", "/data" ]  
  
# Install all of the external components as a single step to reduce layer size  
#  
RUN \  
yum -y update \  
|| exit 1; \  
\  
# Swap out the "Containerized" SystemD for standard SystemD if its installed;
\  
\  
yum -y swap \  
\-- remove systemd-container systemd-container-libs \  
\-- install systemd systemd-libs \  
|| exit 1; \  
\  
# Install other tools we will need; \  
\  
yum -y install \  
lxc \  
dbus \  
|| exit 1; \  
\  
# Deactivate units that will not work in a container; \  
\  
systemctl mask \  
dev-mqueue.mount \  
dev-hugepages.mount \  
sys-kernel-config.mount \  
sys-kernel-debug.mount \  
sys-fs-fuse-connections.mount \  
systemd-remount-fs.service \  
display-manager.service \  
systemd-logind.service \  
console-getty.service \  
getty@tty1.service \  
graphical.target \  
|| exit 1; \  
\  
systemctl enable \  
tmp.mount \  
|| exit 1; \  
\  
# Install docker so we can have a "DinD" environment; \  
\  
curl -sSL https://get.docker.com/ | sh \  
|| exit 1; \  
\  
# Symlink /var/lib/docker into the /data volume to reduce overhead on
overlayfs; \  
\  
ln -sf /data/var/lib/docker /var/lib/docker \  
|| exit 1; \  
\  
ln -sf /data/var/log/docker /var/log/docker \  
|| exit 1; \  
\  
# Make bash the entrypoint till someone changes that; \  
\  
ln -sf /bin/bash /entrypoint.sh \  
|| exit 1; \  
\  
# Cleanup YUM files to reduce image size; \  
\  
yum -y clean all \  
|| exit 1; \  
\  
/bin/true  

