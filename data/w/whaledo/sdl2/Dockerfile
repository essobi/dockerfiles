FROM debian:jessie-slim  
  
ENV MAKE_CONFIG config.mk.dist  
ENV WINDOWS_SDL2_CONFIG /usr/local/cross-
tools/x86_64-w64-mingw32/bin/sdl2-config  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential git
libsdl2-dev gcc-mingw-w64-x86-64 tar zip \  
&& rm -rf /var/lib/apt/lists/*  
  
# Download cross-compiled SDL2 for Windows.  
ADD https://www.libsdl.org/release/SDL2-devel-2.0.5-mingw.tar.gz
/tmp/sdl2-mingw.tar.gz  
# Create destination directories, extract the .tar.gz file, and install it.  
RUN mkdir -p /usr/local/cross-tools/i686-w64-mingw32 \  
&& mkdir -p /usr/local/cross-tools/x86_64-w64-mingw32 \  
&& cd /tmp \  
&& tar xf sdl2-mingw.tar.gz \  
&& make -C SDL2-2.0.5 cross \  
&& rm -rf SDL2-2.0.5  

