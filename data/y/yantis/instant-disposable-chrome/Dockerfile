############################################################  
# Dockerfile for Chrome over SSH with X-Forwarding.  
#  
# Based on Arch Linux  
#  
# FROM yantis/archlinux-tiny  
# FROM yantis/archlinux-small  
# FROM yantis/archlinux-small-ssh-hpn  
# FROM yantis/ssh-hpn-x  
# YOU ARE HERE  
############################################################  
  
FROM yantis/ssh-hpn-x  
MAINTAINER Jonathan Yantis <yantis@yantis.net>  
  
# Don't update  
RUN pacman -Syy --noconfirm && \  
  
# Install Google Chrome  
pacman --noconfirm -S google-chrome libexif libcanberra \  
\--assume-installed python \  
\--assume-installed python-xdg \  
\--assume-installed hwids \  
\--assume-installed kbd \  
\--assume-installed kmod \  
\--assume-installed libseccomp \  
\--assume-installed systemd && \  
  
# generate dbus UUID  
bash -c "dbus-uuidgen > /var/lib/dbus/machine-id" && \  
  
# Cleanup  
rm -r /usr/share/man/* && \  
rm -r /usr/share/doc/* && \  
  
bash -c "echo 'y' | pacman -Scc >/dev/null 2>&1" && \  
paccache -rk0 >/dev/null 2>&1 && \  
pacman-optimize && \  
rm -r /var/lib/pacman/sync/*  
  
CMD ["/init"]  

