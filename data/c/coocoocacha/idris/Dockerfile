FROM dock0/arch  
  
ADD https://github.com/LeifW/Idris-
dev/releases/download/v0.9.20.1/idris-0.9.20.1-1-x86_64.pkg.tar.xz /idris.pkg  
  
RUN pacman --noconfirm -U /idris.pkg  
  
CMD ["idris"]  

