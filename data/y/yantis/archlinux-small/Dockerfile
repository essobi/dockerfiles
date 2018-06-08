###########################################################  
# Dockerfile for custom Arch Linux  
############################################################  
  
FROM yantis/archlinux-tiny  
MAINTAINER Jonathan Yantis <yantis@yantis.net>  
  
ADD service /service  
ADD init /init  
  
# Don't upgrade packages to keep from breaking stuff  
RUN pacman -Syy --noconfirm && \  
# Allow passwordedless sudo for now but we will remove it later.  
pacman --noconfirm -S sudo && \  
echo "docker ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
# Install our programs  
pacman --noconfirm -S zsh wget file patch diffutils htop \  
mlocate expac gzip tar shadow util-linux sed grep awk iputils which && \  
# Add in the s6 stuff since it is small for optional usage.  
ln -s /bin/true /service/s6-svscan-log/finish && \  
# Install yaourt for easy AUR installs but remove later. To much bloat.  
pacman -S --noconfirm yaourt binutils gcc make autoconf fakeroot && \  
# Install s6 and execline from the AUR otherwise amylum breaks them  
runuser -l docker -c "yaourt --noconfirm -S aur/s6 aur/execline aur/skalibs"
&& \  
# Install procps without systemd.  
runuser -l docker -c "yaourt --noconfirm -S procps-ng-nosystemd" && \  
# Install oh-my-zsh from the AUR as it is my PKGBUILD with some fixes the
other doesn't have.  
runuser -l docker -c "yaourt --noconfirm -S aur/oh-my-zsh-git" && \  
runuser -l docker -c "cp /usr/share/oh-my-zsh/zshrc /home/docker/.zshrc" && \  
# Setup root enviroment to be zsh  
cp /usr/share/oh-my-zsh/zshrc /root/.zshrc && \  
chsh -s /usr/bin/zsh root && \  
chsh -s /usr/bin/zsh docker && \  
# Install vim-tiny. Normally we would get it from the herecura repo  
# But it blocks dockerhub for some reason so host it in S3.  
# TODO: Look into pulling and building from:  
# https://github.com/herecura/herecura/tree/master/stable/vim  
wget --content-disposition "http://yantis-scripts.s3.amazonaws.com/vim-
tiny-7.4.692-1-x86_64.pkg.tar.xz" && \  
pacman --noconfirm -U vim-tiny-7.4.692-1-x86_64.pkg.tar.xz && \  
rm vim-tiny-7.4.692-1-x86_64.pkg.tar.xz && \  
# Remove build dependencies.  
pacman --noconfirm -Rs yaourt binutils gcc make autoconf fakeroot git && \  
##########################################################################  
# CLEAN UP SECTION - THIS GOES AT THE END #  
##########################################################################  
localepurge && \  
# Remove info, man and docs  
rm -r /usr/share/info/* && \  
rm -r /usr/share/man/* && \  
rm -r /usr/share/doc/* && \  
# Delete any backup files like /etc/pacman.d/gnupg/pubring.gpg~  
find /. -name "*~" -type f -delete && \  
# Keep only xterm related profiles in terminfo.  
find /usr/share/terminfo/. ! -name "*xterm*" ! -name "*screen*" ! -name
"*screen*" -type f -delete && \  
# Remove anything left in temp.  
rm -r /tmp/* && \  
  
bash -c "echo 'y' | pacman -Scc >/dev/null 2>&1" && \  
paccache -rk0 >/dev/null 2>&1 && \  
pacman-optimize && \  
rm -r /var/lib/pacman/sync/*  
#########################################################################  
  
CMD /usr/bin/zsh  

