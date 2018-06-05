FROM pritunl/archlinux  
MAINTAINER Martin F. acidhunter <npanic@kmpt.nz>  
  
  
RUN curl -o /etc/pacman.d/mirrorlist
"https://www.archlinux.org/mirrorlist/?country=all&protocol=https&ip_version=6&use_mirror_status=on"
&& \  
sed -i 's/^#//' /etc/pacman.d/mirrorlist  
  
ADD aurget.sh /usr/local/bin/aurget  
RUN chmod +x /usr/local/bin/aurget  
  
ADD aurmake.sh /usr/local/bin/aurmake  
RUN chmod +x /usr/local/bin/aurmake  
  
RUN echo 'MAKEFLAGS="-j8"' >> /etc/makepkg.conf  
  
RUN pacman -Syu --force --noconfirm --noprogressbar  
RUN pacman -Sy --force --noconfirm --noprogressbar sudo wget git base-devel
qt5-base qt5-multimedia lzo  
RUN echo '%docker ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
RUN aurget mandelbulber2  
RUN pacman -U --force --noconfirm --noprogressbar /aur/mandelbulber2*.pkg.tar  
  
RUN rm -rf /aur  
  
RUN useradd -m -g users -s /bin/bash docker  
  
ADD init.sh .  
CMD ["sh", "init.sh"]  

