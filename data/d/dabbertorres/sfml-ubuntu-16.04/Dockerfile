from ubuntu:16.04  
run apt update  
run apt upgrade -y  
  
# build dependencies  
run apt install -y \  
build-essential \  
g++ \  
cmake \  
git \  
wget  
  
# runtime dependencies  
run apt install -y \  
libfreetype6-dev \  
libjpeg-dev \  
xorg-dev \  
libxrandr-dev \  
xcb \  
libx11-xcb-dev \  
libxcb-randr0-dev \  
libxcb-image0-dev \  
libgl1-mesa-dev \  
libflac-dev \  
libogg-dev \  
libvorbis-dev \  
libopenal-dev \  
libpthread-stubs0-dev \  
libudev-dev  
  
# build!  
workdir /build  
run git clone https://github.com/SFML/SFML.git  
  
# need to apply a patch  
workdir /build/SFML/  
run wget -O gcc.patch https://gitlab.peach-
bun.com/pinion/SFML/commit/3383b4a472f0bd16a8161fb8760cd3e6333f1782.patch  
run git apply gcc.patch  
  
workdir /build/SFML/build  
run cmake ..  
run make install  
  
# clean up  
workdir /  
run rm -r /build  

