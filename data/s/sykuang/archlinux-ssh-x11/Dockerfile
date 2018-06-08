FROM base/archlinux:latest  
MAINTAINER sykuang <sykuang.tw@gmail.com>  
ENV LANG=en_US.UTF-8  
  
ARG USER=docker  
ARG PASSWORD=docker  
# Add Taiwan and US server to mirrolist  
RUN curl
https://www.archlinux.org/mirrorlist/?country=TW&country=US&protocol=http >>
/etc/pacman.d/mirrorlist && \  
pacman -Syu && \  
# Install develop package  
pacman -S --noconfirm sudo git vim base-devel && \  
# Install yaourt  
echo "[archlinuxfr]" >> /etc/pacman.conf && \  
echo "SigLevel = Never" >> /etc/pacman.conf && \  
echo "Server = http://repo.archlinux.fr/\$arch" >> /etc/pacman.conf && \  
pacman -Syu --noconfirm yaourt && \  
useradd --create-home $USER && \  
echo -e "$USER\n$PASSWORD" | passwd docker && \  
echo "docker ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
# Install HPN and X11  
runuser -l docker -c "yaourt --noconfirm -S openssh-hpn-git" && \  
pacman --noconfirm -S xterm xorg-xclock xorg-xcalc xorg-xauth xorg-xeyes ttf-
droid && \  
# Generate locale en_US  
sed -i 's/#en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \  
locale-gen && \  
# Set SSH Server  
sed -i 's/#Port 22/Port 22/' /etc/ssh/sshd_config && \  
echo "X11Forwarding yes" >> /etc/ssh/sshd_config && \  
echo "X11UseLocalhost no" >> /etc/ssh/sshd_config && \  
runuser -l docker -c "touch /home/docker/.Xauthority" && \  
touch $HOME/.Xauthority && \  
# Cleanup  
rm -r /tmp/* && \  
rm -r /usr/share/man/* && \  
rm -r /usr/share/doc/* && \  
bash -c "echo 'y' | pacman -Scc >/dev/null 2>&1" && \  
paccache -rk0 >/dev/null 2>&1 && \  
pacman-optimize && \  
rm -r /var/lib/pacman/sync/*  
# Add entrypoint.sh  
ADD entrypoint.sh /etc/entrypoint.sh  
  
EXPOSE 22  
ENTRYPOINT ["/bin/bash","/etc/entrypoint.sh"]  

