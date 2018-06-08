## -*- mode: dockerfile -*-  
FROM debian:sid  
RUN apt-get update -q && apt-get install -y \  
git \  
gobject-introspection \  
libgirepository1.0-dev \  
gir1.2-glib-2.0 \  
gir1.2-gudev-1.0 \  
python3-gi \  
locales \  
pkg-config \  
udev \  
libudev-dev \  
libgudev-1.0-dev \  
valac \  
autoconf \  
automake \  
libtool \  
libglib2.0-dev \  
cmake \  
libboost-filesystem-dev \  
libboost-program-options-dev \  
txt2tags \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /usr/local/src  

