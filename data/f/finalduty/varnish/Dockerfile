FROM finalduty/archlinux-base  
MAINTAINER FinalDuty <root@finalduty.me>  
EXPOSE 80  
CMD /usr/bin/varnishd -j none -a 0.0.0.0:80 -f /etc/varnish/default.vcl;
/bin/bash;  
  
RUN pacman -Sy --noconfirm varnish >/dev/null; pacman -Scc --noconfirm
&>/dev/null  

