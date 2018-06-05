#  
# vita-toolchain container based on Archlinux  
# based on devel image w/ packer installed  
#  
# This is a development image, not a production one !  
#  
FROM base/devel  
MAINTAINER Axel Moinet <bullekeup@gmail.com>  
  
# Update pacman  
RUN pacman -Sy --noconfirm pacman package-query && pacman-db-upgrade  
RUN pacman -S --noconfirm archlinux-keyring  
  
# Update the system  
RUN pacman -Syu --noconfirm base-devel git rsync strace curl ca-certificates
ca-certificates-utils  
RUN pacman -Sy --noconfirm ncurses bash-completion rxvt-unicode-terminfo  
RUN pacman -Sy --noconfirm zsh  
  
# Add an user to build and run tests  
RUN useradd -G users,wheel -m -s /usr/bin/zsh devuser  
  
# Add the workspace dir  
RUN mkdir -p /home/workspace  
ADD rootfs.tar.gz /  
RUN pacman -Sy --noconfirm vita-toolchain vita-toolchain-hostlibs  
RUN pacman -Sy --noconfirm vita-toolchain-portlibs vita-toolchain-libs  
RUN pacman -Syu --noconfirm  
RUN pacman -Scc --noconfirm && rm -f /var/cache/pacman/pkg/*  
  
WORKDIR /home/workspace  
USER devuser  
CMD ["/usr/bin/zsh"]  
EXPOSE 1000-2000  

