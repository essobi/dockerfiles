FROM base/archlinux  
MAINTAINER heichblatt  
  
# Workaround for wrong permissions in base image  
# https://github.com/archimg/archlinux/issues/6  
RUN /usr/bin/chmod -v 1777 /tmp  
# Update, install base-devel (incl. sudo), allow sudo for %users  
RUN echo "keyserver-options auto-key-retrieve" >> /etc/pacman.d/gnupg/gpg.conf
&& \  
pacman-key \--init && \  
pacman-key \--populate archlinux && \  
/usr/bin/pacman -Sy \--noconfirm archlinux-keyring && \  
/usr/bin/pacman -Su \--noconfirm && \  
/usr/bin/pacman-db-upgrade && \  
/usr/bin/pacman -S \--noconfirm ca-certificates ca-certificates-mozilla && \  
/usr/bin/pacman -S \--noconfirm base-devel git sudo && \  
/usr/sbin/pacman -Scc \--noconfirm && \  
/usr/sbin/sudo /usr/sbin/ln -sv /usr/bin/core_perl/pod2man /usr/sbin && \  
/usr/sbin/sed -i -e "s/Defaults requiretty.*/ #Defaults requiretty/g"
/etc/sudoers && \  
/usr/sbin/echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
# Add user, group sudo; switch to user  
RUN /usr/sbin/groupadd \--system sudo && \  
/usr/sbin/useradd -m \--groups sudo user  
USER user  
  
# install yaourt  
RUN /usr/bin/mkdir -pv /tmp/yaourt_install && \  
cd /tmp/yaourt_install && \  
/usr/sbin/sudo /usr/sbin/pacman -S \--needed yajl gettext diffutils git
\--noconfirm && \  
/usr/sbin/curl -o PKGBUILD
"https://aur.archlinux.org/cgit/aur.git/plain/PKGBUILD?h=package-query" && \  
/usr/sbin/makepkg PKGBUILD && \  
/usr/sbin/sudo /usr/sbin/pacman -U package-query*.tar.xz \--noconfirm && \  
/usr/sbin/curl -o PKGBUILD
"https://aur.archlinux.org/cgit/aur.git/plain/PKGBUILD?h=yaourt" && \  
/usr/sbin/makepkg PKGBUILD && \  
/usr/sbin/sudo /usr/sbin/pacman -U yaourt*pkg*.tar.xz \--noconfirm && \  
cd && \  
/usr/sbin/rm -rv /tmp/yaourt_install  

