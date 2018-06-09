FROM pritunl/archlinux:latest  
RUN pacman -Syu --noconfirm  
RUN pacman -Sy --noconfirm sudo base-devel desktop-file-utils gettext
gstreamermm gtk-update-icon-cache gtkmm3 cmake git librsvg cxxtest clang ninja
toxcore  
RUN echo "nobody ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
RUN su -c "cd /tmp && curl -O
https://aur.archlinux.org/cgit/aur.git/snapshot/package-query.tar.gz && tar
zxvf package-query.tar.gz && cd package-query && makepkg -si --noconfirm" -s
/bin/bash nobody  
RUN su -c "cd /tmp && curl -O
https://aur.archlinux.org/cgit/aur.git/snapshot/yaourt.tar.gz && tar zxvf
yaourt.tar.gz && cd yaourt && makepkg -si --noconfirm" -s /bin/bash nobody  
RUN su -c "yaourt -Sy --noconfirm flatbuffers" -s /bin/bash nobody  
RUN pacman -Sy ccache --noconfirm  
RUN (echo "y"; echo "y") | pacman -Scc  

