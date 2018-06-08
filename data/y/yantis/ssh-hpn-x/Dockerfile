############################################################  
# Dockerfile for X-Forwarding support over SSH-HPN  
#  
# Based on Arch Linux  
############################################################  
  
FROM yantis/archlinux-small-ssh-hpn  
MAINTAINER Jonathan Yantis <yantis@yantis.net>  
  
# Don't update  
RUN pacman -Syy --noconfirm && \  
  
# Install X related stuff and some fonts.  
pacman --noconfirm -S xterm xorg-xclock xorg-xcalc xorg-xauth xorg-xeyes ttf-
droid && \  
  
# Turn on X11Forwarding and allow remote X11  
echo "X11Forwarding yes" >> /etc/ssh/sshd_config && \  
echo "X11UseLocalhost no" >> /etc/ssh/sshd_config && \  
runuser -l docker -c "touch /home/docker/.Xauthority" && \  
touch $HOME/.Xauthority && \  
  
# Cleanup  
rm -r /usr/share/man/* && \  
rm -r /usr/share/doc/* && \  
bash -c "echo 'y' | pacman -Scc >/dev/null 2>&1" && \  
paccache -rk0 >/dev/null 2>&1 && \  
pacman-optimize && \  
rm -r /var/lib/pacman/sync/*  
  
CMD ["/init"]  

