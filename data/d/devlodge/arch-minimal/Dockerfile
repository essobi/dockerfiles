FROM pritunl/archlinux  
  
RUN pacman --noconfirm -Syu && \  
pacman --noconfirm -S base-devel clang cmake git sdl2 sfml openal freetype2
libpng libjpeg openssh subversion jsoncpp boost boost-libs python2-pip glm
glfw-x11 vulkan-devel && \  
pacman --noconfirm -Sc  
  
# Install lcov  
WORKDIR /tmp  
RUN git clone https://github.com/linux-test-project/lcov.git && \  
cd lcov && make && make install && cd .. && \  
rm -rf lcov  
  
# Install gcovr  
RUN pip2 install gcovr  
  
# Install corrade  
WORKDIR /tmp  
RUN git clone https://github.com/mosra/corrade.git && \  
cd corrade && mkdir build && cd build && \  
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr .. && \  
make -j4 && make install && cd ../../ && \  
rm -rf corrade  
  
# Install magnum  
WORKDIR /tmp  
RUN git clone https://github.com/mosra/magnum.git && \  
cd magnum && \  
mkdir build && \  
cd build && \  
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DWITH_AUDIO=ON
-DWITH_SDL2APPLICATION=ON -DWITH_GLXAPPLICATION=ON
-DWITH_WINDOWLESSGLXAPPLICATION=ON -DWITH_GLXCONTEXT=ON -DWITH_MAGNUMFONT=ON
-DWITH_MAGNUMFONTCONVERTER=ON -DWITH_OBJIMPORTER=ON
-DWITH_TGAIMAGECONVERTER=ON -DWITH_TGAIMPORTER=ON -DWITH_WAVAUDIOIMPORTER=ON
-DWITH_DISTANCEFIELDCONVERTER=ON -DWITH_FONTCONVERTER=ON -DWITH_MAGNUMINFO=ON
.. && \  
make -j4 && \  
make install && \  
cd ../../ && \  
rm -rf magnum  
  
# Install magnum-plugins  
WORKDIR /tmp  
RUN git clone https://github.com/mosra/magnum-plugins.git && \  
cd magnum-plugins && \  
mkdir build && \  
cd build && \  
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr
-DWITH_ANYAUDIOIMPORTER=ON -DWITH_ANYIMAGECONVERTER=ON
-DWITH_ANYIMAGEIMPORTER=ON -DWITH_ANYSCENEIMPORTER=ON -DWITH_DDSIMPORTER=ON
-DWITH_FREETYPEFONT=ON -DWITH_JPEGIMPORTER=ON -DWITH_MINIEXRIMAGECONVERTER=ON
-DWITH_PNGIMPORTER=ON -DWITH_OPENGEXIMPORTER=ON -DWITH_STANFORDIMPORTER=ON
-DWITH_STBIMAGEIMPORTER=ON -DWITH_STBPNGIMAGECONVERTER=ON
-DWITH_STBVORBISAUDIOIMPORTER=ON -DBUILD_STATIC=ON .. && \  
make -j4 && \  
make install && \  
cd ../../ && \  
rm -rf magnum-plugins  

