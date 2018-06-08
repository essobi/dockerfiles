FROM scratch  
MAINTAINER "Arturs Liepins" <arturs@liepins.me>  
  
ENV ARCH_VERSION "2016.07.01"  
ADD busybox /tmp/wget  
ADD busybox /tmp/sh  
ADD tar /tmp/tar  
ADD gzip /tmp/gzip  
  
ENV SHELL /tmp/sh  
RUN [ "/tmp/sh", "-c", "/tmp/wget
http://mirrors.kernel.org/archlinux/iso/$ARCH_VERSION/archlinux-
bootstrap-$ARCH_VERSION-x86_64.tar.gz -O - | /tmp/gzip -d | /tmp/tar
--preserve-permissions --skip-old-files --strip-components=1 -xf -"]  
ENV SHELL /bin/bash  
  
#Clean up  
RUN rm -v /tmp/*  
RUN rm README  
RUN echo "Server = http://mirror.rackspace.com/archlinux/\$repo/os/\$arch" >>
/etc/pacman.d/mirrorlist  
  
#This env variable is checked by systemd  
ENV container docker  
  
RUN pacman-key --init  
RUN pacman-key --populate archlinux  
RUN pacman -Syyu --noconfirm --needed --noprogressbar  
RUN pacman-db-upgrade  
RUN yes | pacman -Scc  

