FROM nfnty/arch-mini:latest  
  
RUN pacman -Syu --noconfirm && \  
pacman -S --noconfirm \  
git \  
cmake \  
ninja \  
make \  
gcc \  
pkg-config \  
assimp \  
libepoxy \  
sdl2 \  
sdl2_mixer \  
bullet \  
mesa-libgl \  
unittestpp \  
freeimage \  
tinyxml2  
  
RUN pacman -Scc  
  
RUN mkdir /data  
  
WORKDIR /data  
  
CMD cmake -G Ninja ./; ninja -j 4; ninja tests;  

