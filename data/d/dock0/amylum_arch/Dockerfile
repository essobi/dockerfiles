FROM dock0/arch  
MAINTAINER akerl <me@lesaker.org>  
ADD amylum.conf /etc/pacman.d/amylum.conf  
RUN cat /etc/pacman.d/amylum.conf >> /etc/pacman.conf && rm
/etc/pacman.d/amylum.conf  
ADD keyrings/* /usr/share/pacman/keyrings/  
RUN pacman-key --populate amylum  
RUN pacman -Syu  

