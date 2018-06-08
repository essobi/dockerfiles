FROM finalduty/archlinux  
MAINTAINER heliary rydesun@gmail.com  
  
RUN curl
'https://www.archlinux.org/mirrorlist/?country=CN&protocol=http&ip_version=4'
> /etc/pacman.d/mirrorlist \  
&& sed -i 's/^#//' /etc/pacman.d/mirrorlist \  
&& curl 'https://raw.githubusercontent.com/archlinuxcn/mirrorlist-
repo/master/README.md' | grep '^Server' > /etc/pacman.d/archlinuxcn-mirrorlist
\  
# Global CDN has no nodes in mainland China  
&& sed -i '/cdn/s/^/#/' /etc/pacman.d/archlinuxcn-mirrorlist \  
&& echo '[archlinuxcn]' >> /etc/pacman.conf \  
&& echo 'SigLevel = Optional TrustedOnly' >> /etc/pacman.conf \  
&& echo 'Include = /etc/pacman.d/archlinuxcn-mirrorlist' >> /etc/pacman.conf \  
&& pacman -Syy \  
&& pacman -S \--noconfirm archlinuxcn-keyring \  
&& ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \  
&& rm /var/cache/pacman/pkg/*  
  
CMD /bin/bash  

