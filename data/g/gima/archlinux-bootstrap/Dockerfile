FROM scratch  
MAINTAINER Gima  
  
ADD busybox-x86_64.tar.bz2 /  
ADD bootstrap.sh /  
ADD https://mirrors.kernel.org/archlinux/iso/2014.10.01/archlinux-
bootstrap-2014.10.01-x86_64.tar.gz /archlinux-bootstrap-x86_64.tar.gz  
  
# magic option "xtrace" found from
http://git.busybox.net/busybox/tree/shell/ash.c#n212  
# xtrace makes sh echo executed commands  
RUN ["/busybox", "sh", "-o", "xtrace", "bootstrap.sh"]  

