FROM yantis/archlinux-tiny  
MAINTAINER Karl Hepworth <karl.hepworth@gmail.com>  
  
ADD init /init  
  
# Don't upgrade packages to keep from breaking stuff  
RUN pacman -Syy --noconfirm  
  
# Allow passwordedless sudo for now but we will remove it later.  
RUN pacman --noconfirm -S sudo && \  
echo "docker ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
# Install our programs  
RUN pacman --noconfirm -S \  
zsh wget file patch diffutils htop \  
mlocate expac gzip tar shadow util-linux \  
sed grep awk iputils which  
  
# Install procps without systemd.  
RUN runuser -l docker -c "yaourt --noconfirm -S procps-ng-nosystemd"  
  
# Remove build dependencies.  
RUN pacman --noconfirm -Rs yaourt binutils gcc make autoconf fakeroot git
localepurge  
  
# Remove info, man and docs  
RUN rm -r /usr/share/info/* && \  
RUN rm -r /usr/share/man/* && \  
RUN rm -r /usr/share/doc/* && \  
  
# Delete any backup files like /etc/pacman.d/gnupg/pubring.gpg~  
RUN find /. -name "*~" -type f -delete  
  
# Keep only xterm related profiles in terminfo.  
RUN find /usr/share/terminfo/. ! -name "*xterm*" ! -name "*screen*" ! -name
"*screen*" -type f -delete && \  
  
# Remove anything left in temp.  
RUN rm -r /tmp/* && \  
  
RUN bash -c "echo 'y' | pacman -Scc >/dev/null 2>&1" && \  
paccache -rk0 >/dev/null 2>&1 && \  
pacman-optimize && \  
rm -r /var/lib/pacman/sync/*  
  
CMD /usr/bin/bash  

