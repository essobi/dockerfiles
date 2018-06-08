  
# build base  
FROM archimg/base:2017.10.01  
# repository baseline  
ENV ARCH_DATE="2017/11/01"  
ENV ARCH_BASE="http://archive.archlinux.org/repos/$ARCH_DATE"  
# freeze packages  
RUN \  
echo Server=$ARCH_BASE'/$repo/os/$arch' > /etc/pacman.d/mirrorlist && \  
true  
  
# package install  
ENV PACRUN="pacman --needed --noconfirm --noprogressbar"  
# update system packages  
RUN \  
$PACRUN -Sy && \  
$PACRUN -S pacman archlinux-keyring && \  
$PACRUN -Syu && \  
true  
  
# provision systemd  
RUN $PACRUN -S \  
systemd  
  
# use non-gui target  
RUN systemctl set-default multi-user.target  
  
# declare systemd context  
ENV container docker  
  
# required systemd mount  
VOLUME [ "/sys/fs/cgroup" ]  
  
# default command is system init  
CMD ["/usr/lib/systemd/systemd"]  

