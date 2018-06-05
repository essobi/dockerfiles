FROM desiato/archlinux-bootstrap  
  
RUN pacman --noconfirm -Syyu && \  
pacman --noconfirm --needed -S diffutils file gawk gettext grep gzip inetutils
iputils less logrotate procps-ng psmisc sed shadow sysfsutils tar util-linux
which && \  
echo -e 'y\ny' | pacman -Scc && \  
rm -r /usr/share/man/* && \  
sed -i '/^#en_US.UTF-8/s/^#//' /etc/locale.gen && \  
locale-gen && \  
echo 'LANG=en_US.UTF-8' > /etc/locale.conf && \  
ls -d /usr/share/locale/* | egrep -v 'alias|en_US' | xargs rm -rf  

