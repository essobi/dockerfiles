############################################################  
# Dockerfile for Thunderbird both single user or SSH with X-Forwarding.  
#  
# Based on Arch Linux  
#  
# FROM yantis/archlinux-tiny  
# FROM yantis/archlinux-small  
# FROM yantis/archlinux-small-ssh-hpn  
# FROM yantis/ssh-hpn-x  
# YOU ARE HERE  
# Forked from yantis/docker-thunderbird by IronicBadger  
############################################################  
  
FROM yantis/ssh-hpn-x  
MAINTAINER Jonathan Yantis <yantis@yantis.net>  
  
# Update and force a refresh of all package lists even if they appear up to
date.  
RUN pacman -Syu --noconfirm && \  
  
# Install program  
pacman --noconfirm -S thunderbird \  
libcanberra \  
\--assume-installed hwids \  
\--assume-installed kbd \  
\--assume-installed kmod \  
\--assume-installed libseccomp \  
\--assume-installed systemd && \  
  
# Cleanup  
rm -r /usr/share/man/* && \  
rm -r /usr/share/doc/* && \  
bash -c "echo 'y' | pacman -Scc >/dev/null 2>&1" && \  
paccache -rk0 >/dev/null 2>&1 && \  
pacman-optimize && \  
rm -r /var/lib/pacman/sync/*  
  
CMD ["/init"]  

