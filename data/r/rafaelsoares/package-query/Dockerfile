FROM rafaelsoares/archlinux:2016-04-09-devel  
MAINTAINER Rafael Soares  
  
# Building the package  
RUN /bin/sh -c "cd /home/guest && git clone https://aur.archlinux.org/package-
query.git && cd package-query && makepkg -sf"  

