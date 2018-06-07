FROM nfnty/arch-mini  
  
RUN pacman -Syyu --noconfirm awk binutils file fakeroot git python python-
pandocfilters make ttf-linux-libertine ghostscript fig2dev texlive-latexextra
texlive-fontsextra  
  
# install pandoc from AUR  
WORKDIR /tmp  
RUN curl -L -O https://aur.archlinux.org/cgit/aur.git/snapshot/pandoc-
bin.tar.gz  
RUN tar xzf pandoc-bin.tar.gz  
RUN chmod 777 pandoc-bin  
WORKDIR /tmp/pandoc-bin  
RUN useradd -M buildpkg  
USER buildpkg  
RUN makepkg -c --nodeps  
USER root  
RUN pacman -U --noconfirm pandoc-bin-*  
WORKDIR /  
  
# cleanup  
RUN rm -rf /tmp/*  
RUN paccache -rfk0  
  
RUN mkdir /gitlab  
ENV HOME=/gitlab  
  
# All builds will be done in home dir  
WORKDIR $HOME  
  
CMD ["/bin/bash"]  

