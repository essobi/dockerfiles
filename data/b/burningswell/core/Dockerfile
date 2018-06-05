FROM pritunl/archlinux:2016-11-12  
MAINTAINER Roman Scherer <roman@burningswell.com>  
  
ENV LEIN_ROOT 1  
ENV PACMAN_OPTS --noconfirm --noprogressbar  
  
RUN pacman -S $PACMAN_OPTS curl jdk8-openjdk  
RUN curl
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein >
/usr/local/bin/lein  
RUN chmod 755 /usr/local/bin/lein  
RUN lein version  

