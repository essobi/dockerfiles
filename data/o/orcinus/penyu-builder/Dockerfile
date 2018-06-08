FROM alpine:3.6  
MAINTAINER ibnu yahya <anak10thn@gmail.com>  
  
ENV LANG=C.UTF-8 LC_ALL=C  
  
RUN apk --update add bash sudo build-base apk-tools alpine-conf busybox
fakeroot syslinux xorriso shadow abuild git coreutils squashfs-tools  
  
RUN adduser -s /bin/sh -S am -G abuild; echo "am ALL=(ALL) NOPASSWD:ALL" >>
/etc/sudoers;  
  
WORKDIR /tmp  
USER am

