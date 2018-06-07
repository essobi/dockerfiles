FROM debian:sid  
ARG DEBIAN_FRONTEND="noninteractive"  
ARG LANG="C.UTF-8"  
ARG LC_ALL="C.UTF-8"  
ARG CACHING_PROXY=""  
ENV DEBIAN_FRONTEND="noninteractive" LANG="C.UTF-8" LC_ALL="C.UTF-8"  
ENV CACHING_PROXY=""  
RUN apt-get update  
RUN apt-get install -y -f adduser \  
libegl1-mesa-dev \  
libwayland-egl1-mesa \  
libwayland-egl1 \  
libgles2-mesa \  
libgles2 \  
libc6 \  
libcairo2-dev \  
libcolord-dev \  
libdbus-1-dev \  
libdrm-dev \  
libgbm-dev \  
libglib2.0-dev \  
libinput-dev \  
libjpeg62-turbo \  
liblcms2-dev \  
libmtdev-dev \  
libpam0g-dev \  
libpango1.0-dev \  
libpangocairo-1.0-0 \  
libpixman-1-dev \  
libpng-dev \  
libsystemd-dev \  
libudev-dev \  
libwayland-client0 \  
libwayland-cursor0 \  
libwayland-server0 \  
libwayland-dev \  
libx11-dev \  
libx11-xcb-dev \  
libxcb-composite0-dev \  
libxcb-render0-dev \  
libxcb-shape0-dev \  
libxcb-shm0-dev \  
libxcb-xfixes0-dev \  
libxcb-xkb-dev \  
libxcb1-dev \  
libxcursor-dev \  
libxkbcommon-dev \  
libstd-rust-dev \  
rustc cargo dh-cargo  
RUN adduser --disabled-password --home /home/build --shell /bin/bash
--disabled-password --gecos "build" build  
  
#FROM clux/muslrust  
  
COPY . /home/build/fireplace  
  
#USER root  
RUN chown build:build -R /home/build/fireplace  
USER build  
  
WORKDIR /home/build/fireplace/  
RUN make build  
CMD bash  

