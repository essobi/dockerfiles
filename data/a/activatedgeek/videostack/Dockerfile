FROM ubuntu:14.04  
  
MAINTAINER Sanyam Kapoor "1sanyamkapoor@gmail.com"  
  
RUN apt-get -y update &&\  
apt-get install -y --no-install-recommends \  
software-properties-common \  
python-software-properties &&\  
add-apt-repository -y ppa:mc3man/trusty-media &&\  
# needed for libfaac-dev  
echo "deb http://us.archive.ubuntu.com/ubuntu trusty main multiverse" >>
/etc/apt/sources.list &&\  
apt-get -y update &&\  
# install dependencies for Mesa DRI Drivers  
apt-get install -y \  
ffmpeg \  
imagemagick \  
libav-tools \  
libavcodec-extra \  
libfreetype6-dev \  
libfaac-dev \  
libjpeg-dev \  
libsdl2-dev \  
libsox-fmt-mp3 \  
python \  
python-pip \  
python-opencv \  
sox \  
zlib1g-dev &&\  
ln -s /usr/lib/x86_64-linux-gnu/libfaac.so /usr/lib &&\  
ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib &&\  
ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib &&\  
ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib &&\  
apt-get install -y python-dev g++ &&\  
pip install \  
freetype-py==1.0.2 \  
numpy==1.11.0 \  
Pillow==3.3.0 \  
PyOpenGL==3.1.0 \  
PyOpenGL-accelerate==3.1.0 \  
PySDL2==0.9.3 &&\  
apt-get install -y --no-install-recommends \  
git \  
g++ \  
automake \  
libtool \  
libpthread-stubs0-dev \  
xserver-xorg-dev \  
x11proto-xinerama-dev \  
libx11-xcb-dev \  
libxcb-glx0-dev \  
libxrender-dev \  
xutils-dev &&\  
apt-get build-dep -y libgl1-mesa-dri libxcb-glx0-dev &&\  
pip install Mako &&\  
git clone git://anongit.freedesktop.org/git/mesa/mesa /tmp/mesa &&\  
git clone git://anongit.freedesktop.org/git/mesa/drm /tmp/drm &&\  
export LIBDIR=/usr/lib/x86_64-linux-gnu &&\  
# build and install DRM from source  
cd /tmp/drm &&\  
./autogen.sh --prefix=/usr --libdir=${LIBDIR} &&\  
make && make install &&\  
# build and install Mesa3D from source  
cd /tmp/mesa &&\  
./autogen.sh --prefix=/usr \  
\--libdir=${LIBDIR} \  
\--with-gallium-drivers=swrast \  
\--without-dri-drivers \  
\--disable-dri3 \  
\--enable-glx-tls \  
\--enable-texture-float &&\  
make && make install &&\  
pip uninstall -y Mako &&\  
apt-get remove --purge -y \  
git \  
g++ \  
automake \  
libtool \  
libpthread-stubs0-dev \  
xserver-xorg-dev \  
x11proto-xinerama-dev \  
libx11-xcb-dev \  
libxcb-glx0-dev \  
libxrender-dev \  
xutils-dev \  
software-properties-common \  
python-dev \  
python-software-properties &&\  
apt-get -y autoremove && apt-get -y autoclean &&\  
rm -rf /var/lib/apt/lists/* /tmp/*  

