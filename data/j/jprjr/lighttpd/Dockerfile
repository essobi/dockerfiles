FROM jprjr/arch  
  
MAINTAINER John Regan <john@jrjrtech.com>  
RUN pacman -Syy --noconfirm --quiet > /dev/null  
  
RUN pacman -S --noconfirm --quiet --needed \  
lighttpd openssl >/dev/null 2>/dev/null  
  
EXPOSE 80  
EXPOSE 443  
VOLUME /etc/lighttpd  
  
ENTRYPOINT ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]  

