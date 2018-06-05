FROM pehowell/arch-dumbinit  
LABEL maintainer="Paul Howell <paul.howell+docker@gmail.com>"  
  
ENV TERM xterm  
  
RUN set -euxo pipefail && \  
echo $'[archlinuxfr]\n\  
SigLevel = Never\n\  
Server = http://repo.archlinux.fr/$arch\n' >> /etc/pacman.conf  
  
ENV TEMP_PKG "autoconf binutils fakeroot gcc make patch sudo yaourt"  
ENV NEEDED_PKG "gnu-netcat"  
COPY start.sh /home/ib/start.sh  
COPY jts.ini /home/ib/jts.ini  
  
RUN set -euxo pipefail && \  
pacman -Syu --noconfirm ${TEMP_PKG} ${NEEDED_PKG} && \  
useradd -G wheel ib && \  
chown -R ib:ib /home/ib && \  
chmod +x /home/ib/start.sh && \  
sed -i 's/^# \\(.*\\)NOPASSWD\\(.*\\)$/\1NOPASSWD\2/' /etc/sudoers && \  
sudo -u ib yaourt -S --noconfirm --nocolor --m-arg "--skipchecksums" ib-tws &&
\  
sudo -u ib yaourt -S --noconfirm --nocolor ib-controller localepurge && \  
localepurge && \  
pacman -Runs --noconfirm $(pacman -Qtdq) && \  
pacman -Rdd --noconfirm gtk2 guile icu llvm-libs mesa perl systemd ttf-dejavu
xorg-fonts-misc wayland ${TEMP_PKG} && \  
mkdir -p /var/run/xvfb && \  
rm -rf /usr/share/man/* && \  
rm -rf /usr/share/doc/*  
  
VOLUME /home/ib/config  
WORKDIR /home/ib  
  
EXPOSE 4001  
# HEALTHCHECK --interval=5s --timeout=3s CMD nc -z localhost 4001  
CMD ["/bin/bash", "/home/ib/start.sh"]  

