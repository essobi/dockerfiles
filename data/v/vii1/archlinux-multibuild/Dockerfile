# MingW64 + Qt5 for cross-compile builds to Windows  
# Based on ArchLinux image  
# Note: pacman cache is cleared to reduce image size by a few 100 mbs in
total.  
# `pacman -Scc --noconfirm` responds 'N' by default to removing the cache,
hence  
# the echo mechanism.  
# BUILD ARGS:  
# WINE=1 -> install Wine  
# ARCH -> target arch. Any or both of: x86 amd64  
# PLATFORM -> target platform. Any or both of: windows linux  
FROM base/archlinux:latest  
LABEL maintainer="Gabriel Lorenzo <gabriel.lorenzo@simloc.es>"  
  
# Add mirrorlist (USA to optimize Docker Cloud autobuilds)  
RUN curl -s
'https://www.archlinux.org/mirrorlist/?country=US&protocol=https&ip_version=4'
|cut -c 2- > /etc/pacman.d/mirrorlist  
  
# Update base system  
RUN pacman -Sy --noconfirm --noprogressbar archlinux-keyring \  
&& pacman-key --populate \  
&& pacman -Su --noconfirm --noprogressbar --needed pacman \  
&& pacman-db-upgrade \  
&& pacman -Su --noconfirm --noprogressbar ca-certificates \  
&& trust extract-compat \  
&& pacman -Syyu --noconfirm --noprogressbar --needed \  
&& (echo -e "y\ny\n" | pacman -Scc)  
  
# Multilib repo  
RUN echo "[multilib]" >> /etc/pacman.conf \  
&& echo "Include = /etc/pacman.d/mirrorlist" >> /etc/pacman.conf \  
&& pacman -Sy  
  
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
# Todos los paquetes que no dependan de ARGs aquí  
RUN pacman -S --noconfirm --noprogressbar --needed \  
make \  
ninja \  
git \  
binutils \  
patch \  
meson \  
unzip \  
&& (echo -e "y\ny\n" | pacman -Scc)  
  
COPY install_packages.sh /root/  
RUN chmod +x /root/install_packages.sh  
  
# 0 = sin wine, 1 = con wine (32 y 64)  
ARG WINE  
# x86, amd64 o los dos  
ARG ARCH  
# windows, linux o los dos  
ARG PLATFORM  
  
# Capa 1  
RUN /root/install_packages.sh windows  
# Capa 2  
RUN /root/install_packages.sh linux  
# Capa 3  
RUN /root/install_packages.sh wine  
  
COPY Qt5CoreMacros.cmake /usr/i686-w64-mingw32/lib/cmake/Qt5Core/  
COPY Qt5CoreMacros.cmake /usr/x86_64-w64-mingw32/lib/cmake/Qt5Core/  
  
# Create devel user...  
RUN useradd -m -d /home/devel -u 1000 -U -G users,tty -s /bin/bash devel  
USER devel  
ENV HOME=/home/devel  
WORKDIR /home/devel  
  
# ... but don't use it on the next image builds  
ONBUILD USER root  
ONBUILD WORKDIR /  

