FROM dock0/arch  
RUN pacman -Sy --needed --noconfirm base-devel git curl sudo && pacman -Scc
--noconfirm  
  
# Add a user to use in the docker container  
RUN groupadd -g 42 awesome && useradd -r -u 42 --create-home -g awesome
awesome  
  
# Give user root access via sudo  
RUN echo "awesome ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
# Do some system setup as the root user  
RUN mkdir /.cache && sudo chown awesome:awesome /.cache/  
RUN echo 'EDITOR=false' > /etc/profile.d/editor.sh && chmod +x
/etc/profile.d/editor.sh  
RUN echo 'EDITOR=false' >> /etc/bash.bashrc  
  
# Improve build times for makepkg installs  
RUN echo 'MAKEFLAGS="-j4"' >> /etc/makepkg.conf  
RUN echo 'BUILDDIR="/tmp/makepkg"' >> /etc/makepkg.conf  
RUN echo 'BUILDENV=(!distcc color !ccache !check !sign)' >> /etc/makepkg.conf  
  
# Become the user  
USER awesome  
  
# Install yay AUR helper  
RUN mkdir -p /tmp/yay && cd /tmp/yay && . /etc/profile.d/perlbin.sh && curl -o
PKGBUILD https://aur.archlinux.org/cgit/aur.git/plain/PKGBUILD?h=yay-bin &&
makepkg PKGBUILD --skippgpcheck --needed --install --noconfirm --rmdeps &&
sudo pacman -Scc --noconfirm && rm -rf /tmp/yay && rm -rf /tmp/makepkg  
RUN yay -S --needed --noconfirm --editor false \--answerclean None
--answeredit None --answerupgrade None --save  

