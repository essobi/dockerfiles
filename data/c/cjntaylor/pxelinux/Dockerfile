FROM alpine:latest  
MAINTAINER Colin Taylor <cjntaylor@gmail.com>  
  
RUN apk add --update syslinux && rm -rf /var/cache/apk/*  
RUN mkdir -p /pxelinux && cp -a /usr/share/syslinux/lpxelinux.0
/usr/share/syslinux/ldlinux.c32 /usr/share/syslinux/libcom32.c32
/usr/share/syslinux/libutil.c32 /usr/share/syslinux/libmenu.c32
/usr/share/syslinux/menu.c32 /usr/share/syslinux/cmd.c32
/usr/share/syslinux/reboot.c32 /pxelinux  

