FROM debian:8  
LABEL maintainer="Wilmar den Ouden <info@wilmardenouden.nl>"  
  
ENV container docker  
  
RUN if [ $(command -v apt-get) ]; then apt-get update && apt-get upgrade -y &&
apt-get install -y systemd systemd-sysv python-minimal sudo bash ca-
certificates && apt-get clean; \  
elif [ $(command -v dnf) ]; then dnf makecache && dnf --assumeyes install
python sudo python-devel python2-dnf bash && dnf clean all; \  
elif [ $(command -v yum) ]; then yum makecache fast && yum update -y && yum
install -y python sudo yum-plugin-ovl bash && sed -i 's/plugins=0/plugins=1/g'
/etc/yum.conf && yum clean all; \  
elif [ $(command -v zypper) ]; then zypper refresh && zypper update -y &&
zypper install -y python sudo bash python-xml && zypper clean -a; \  
elif [ $(command -v apk) ]; then apk update && apk add --no-cache python sudo
bash ca-certificates; fi  
  
# We only want few core services run in the container.  
RUN systemctl mask \  
dev-hugepages.mount \  
sys-fs-fuse-connections.mount \  
sys-kernel-config.mount \  
display-manager.service \  
getty@.service \  
systemd-logind.service \  
systemd-remount-fs.service \  
getty.target \  
graphical.target \  
console-getty.service \  
systemd-vconsole-setup.service \  
kmod-static-nodes.service \  
&& systemctl set-default multi-user.target  
  
STOPSIGNAL SIGRTMIN+3  
ENTRYPOINT ["/sbin/init"]  

