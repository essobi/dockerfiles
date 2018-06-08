FROM devlodge/arch-minimal  
  
RUN pacman --noconfirm -Syy && \  
pacman --noconfirm -Syu && \  
pacman --noconfirm -S texlive-most emacs-nox gnuplot ttf-dejavu pygmentize
biber && \  
pacman --noconfirm -Sc  
  
# Install Metropolis theme  
WORKDIR /tmp  
RUN git clone https://github.com/matze/mtheme.git && \  
cd mtheme && \  
make sty && \  
make install && \  
cd .. && \  
rm -rf mtheme  

