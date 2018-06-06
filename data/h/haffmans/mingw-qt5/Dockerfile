# MingW64 + Qt5 for cross-compile builds to Windows  
# Based on ArchLinux image  
# Note: pacman cache is cleared to reduce image size by a few 100 mbs in
total.  
# `pacman -Scc --noconfirm` responds 'N' by default to removing the cache,
hence  
# the echo mechanism.  
  
FROM base/archlinux:latest  
MAINTAINER Wouter Haffmans <wouter@simply-life.net>  
  
# Update base system  
RUN pacman -Sy --noconfirm --noprogressbar archlinux-keyring \  
&& pacman-key --populate \  
&& pacman -Su --noconfirm --noprogressbar pacman \  
&& pacman-db-upgrade \  
&& pacman -Su --noconfirm --noprogressbar ca-certificates \  
&& trust extract-compat \  
&& pacman -Syyu --noconfirm --noprogressbar \  
&& (echo -e "y\ny\n" | pacman -Scc)  
  
# Add martchus.no-ip.biz repo for mingw binaries  
RUN echo "[ownstuff]" >> /etc/pacman.conf \  
&& echo "SigLevel = Optional TrustAll" >> /etc/pacman.conf \  
&& echo "Server = https://martchus.no-ip.biz/repo/arch/\$repo/os/\$arch " >>
/etc/pacman.conf \  
&& pacman -Sy  
  
# Add mingw-repo  
RUN echo "[mingw-w64]" >> /etc/pacman.conf \  
&& echo "SigLevel = Optional TrustAll" >> /etc/pacman.conf \  
&& echo "Server =
http://downloads.sourceforge.net/project/mingw-w64-archlinux/\$arch" >>
/etc/pacman.conf \  
&& pacman -Sy  
  
# Add some useful packages to the base system  
RUN pacman -S --noconfirm --noprogressbar \  
imagemagick \  
make \  
ninja \  
git \  
binutils \  
patch \  
&& (echo -e "y\ny\n" | pacman -Scc)  
  
# Install MingW packages  
RUN pacman -S --noconfirm --noprogressbar \  
mingw-w64-binutils \  
mingw-w64-crt \  
mingw-w64-gcc \  
mingw-w64-headers \  
mingw-w64-winpthreads \  
mingw-w64-bzip2 \  
mingw-w64-cmake \  
mingw-w64-expat \  
mingw-w64-fontconfig \  
mingw-w64-freeglut \  
mingw-w64-freetype2 \  
mingw-w64-gettext \  
mingw-w64-libdbus \  
mingw-w64-libiconv \  
mingw-w64-libjpeg-turbo \  
mingw-w64-libpng \  
mingw-w64-libtiff \  
mingw-w64-libxml2 \  
mingw-w64-mariadb-connector-c \  
mingw-w64-nsis \  
mingw-w64-openssl \  
mingw-w64-openjpeg \  
mingw-w64-openjpeg2 \  
mingw-w64-pcre \  
mingw-w64-pdcurses \  
mingw-w64-pkg-config \  
mingw-w64-qt5-base \  
mingw-w64-qt5-base-static \  
mingw-w64-qt5-declarative \  
mingw-w64-qt5-graphicaleffects \  
mingw-w64-qt5-imageformats \  
mingw-w64-qt5-location \  
mingw-w64-qt5-multimedia \  
mingw-w64-qt5-quickcontrols \  
mingw-w64-qt5-script \  
mingw-w64-qt5-sensors \  
mingw-w64-qt5-svg \  
mingw-w64-qt5-webkit \  
mingw-w64-qt5-websockets \  
mingw-w64-qt5-winextras \  
mingw-w64-readline \  
mingw-w64-sdl2 \  
mingw-w64-sqlite \  
mingw-w64-termcap \  
mingw-w64-tools \  
mingw-w64-zlib \  
&& pacman -S --noconfirm --noprogressbar \  
\--force \  
# Conflicts with qt5-base  
mingw-w64-qt5-tools \  
# Requires qt5-tools  
mingw-w64-qt5-quick1 \  
# Requires qt5-tools  
mingw-w64-qt5-translations \  
&& (echo -e "y\ny\n" | pacman -Scc)  
  
ADD Qt5CoreMacros.cmake /usr/i686-w64-mingw32/lib/cmake/Qt5Core/  
ADD Qt5CoreMacros.cmake /usr/x86_64-w64-mingw32/lib/cmake/Qt5Core/  
# Create devel user...  
RUN useradd -m -d /home/devel -u 1000 -U -G users,tty -s /bin/bash devel  
USER devel  
ENV HOME=/home/devel  
WORKDIR /home/devel  
  
# ... but don't use it on the next image builds  
ONBUILD USER root  
ONBUILD WORKDIR /  

