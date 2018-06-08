# Copying and distribution of this file, with or without modification,  
# are permitted in any medium without royalty.  
# This file is offered as-is, without any warranty.  
  
FROM fedora  
  
RUN set -x \  
&& yum install -y \  
fftw-devel \  
gcc-c++ \  
gstreamer1-devel \  
gstreamer1-plugins-base-devel \  
meson \  
ninja-build \  
mingw64-fftw \  
mingw64-gcc-c++ \  
mingw64-gstreamer1 \  
mingw64-gstreamer1-plugins-base \  
mingw64-pkg-config \  
pkgconf \  
python3 \  
python3-numpy \  
wine-core \  
&& rm -rf /var/cache/dnf/*  
  
COPY fedora-win64.reg /  
RUN set -x \  
&& wine64 regedit /C /fedora-win64.reg \  
&& wineserver -w \  
&& rm /fedora-win64.reg  
  
COPY fedora-win64.meson-cross /root/.local/share/meson/cross/fedora-win64  

