FROM base/devel:latest  
MAINTAINER Karol Gusak "dev@kar.gs"  
# Temporarily disable pacman signing  
RUN sed -i 's/SigLevel = Required DatabaseOptional/SigLevel = Never/'
/etc/pacman.conf  
  
# Update mirrorlist based on local speed  
RUN cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.backup  
RUN sed -i 's/^#//' /etc/pacman.d/mirrorlist.backup  
RUN rankmirrors -n 6 /etc/pacman.d/mirrorlist.backup >
/etc/pacman.d/mirrorlist  
  
RUN pacman -Sy  
RUN pacman --noconfirm -S vim xterm  
RUN yaourt --noconfirm -S xpra-winswitch  
RUN xpra start :10  
  
ENTRYPOINT DISPLAY=:10 xterm  

