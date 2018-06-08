FROM scratch  
MAINTAINER binhex  
  
# additional files  
##################  
  
# add statically linked busybox  
ADD build/busybox/busybox /bootstrap/busybox  
  
# unpack tarball  
################  
  
# symlink busybox utilities to /bootstrap folder  
RUN ["/bootstrap/busybox", "--install", "-s", "/bootstrap"]  
  
# run busybox bourne shell and use sub shell to execute busybox utils  
# note, do not line wrap the below command, as it will fail, looking for
/bin/sh  
RUN ["/bootstrap/sh", "-c", "/bootstrap/wget -O /bootstrap/archlinux.tar.bz2
https://github.com/binhex/arch-scratch/releases/download/2018032800/arch-
root.tar.bz2; /bootstrap/tar -xvjf /bootstrap/archlinux.tar.bz2 -C /;
/bootstrap/rm -rf /bootstrap /.dockerenv /.dockerinit /usr/share/info/*"]  
  
# set entry point as /bin/bash  
CMD ["/bin/bash"]

