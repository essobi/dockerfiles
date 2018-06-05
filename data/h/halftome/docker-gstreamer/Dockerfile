FROM ubuntu:rolling  
  
ARG GST_VERSION=1.14.0  
  
RUN apt-get -y update  
  
# Install dependencies  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \  
autoconf \  
automake \  
autopoint \  
bison \  
flex \  
libtool \  
yasm \  
nasm \  
git-core \  
build-essential \  
gettext \  
meson \  
libavfilter-dev \  
libglib2.0-dev \  
libgirepository1.0-dev \  
libpthread-stubs0-dev \  
libssl-dev \  
liborc-dev \  
libmpg123-dev \  
libmp3lame-dev \  
libsoup2.4-dev \  
libshout3-dev \  
libpulse-dev \  
libva-dev \  
libxv-dev \  
libalsa-ocaml-dev \  
libcdparanoia-dev \  
libopus-dev \  
libpango1.0-dev \  
libvisual-0.4-dev \  
libvorbisidec-dev \  
libaa1-dev \  
libcaca-dev \  
libdv4-dev \  
libflac-dev \  
libjack-dev \  
libtag1-dev \  
libdrm-dev \  
libvpx-dev \  
libwavpack-dev \  
libass-dev \  
libzbar-dev \  
libx265-dev \  
libx264-dev \  
libwildmidi-dev \  
libvulkan-dev \  
libx11-dev \  
libxrandr-dev \  
libwayland-dev \  
wayland-protocols \  
libwebp-dev \  
libwebrtc-audio-processing-dev \  
libvdpau-dev \  
libsrtp0-dev \  
libvo-aacenc-dev \  
libvo-amrwbenc-dev \  
libbs2b-dev \  
libdc1394-22-dev \  
libdts-dev \  
libfaac-dev \  
libfaad-dev \  
libfdk-aac-dev \  
libfluidsynth-dev \  
libcurl-ocaml-dev \  
libgme-dev \  
libgsm1-dev \  
librtmp-dev \  
libcurl-ocaml-dev \  
libjpeg-turbo8-dev \  
liba52-0.7.4-dev \  
libcdio-dev \  
libtwolame-dev \  
libx264-dev \  
libmpeg2-4-dev \  
libsidplay1-dev \  
gobject-introspection \  
libudev-dev \  
python3-pip \  
python3-gi \  
python-gi-dev  
  
# Fetch and build GStreamer  
RUN git clone -b $GST_VERSION --depth 1
git://anongit.freedesktop.org/git/gstreamer/gstreamer && \  
cd gstreamer && \  
git checkout $GST_VERSION && \  
meson build --prefix=/usr --libdir=/usr/lib --buildtype=release && \  
ninja -C build -j `nproc` && \  
ninja -C build install && \  
cd .. && \  
rm -rvf /gstreamer  
  
# Fetch and build gst-plugins-base  
RUN git clone -b $GST_VERSION --depth 1
git://anongit.freedesktop.org/git/gstreamer/gst-plugins-base && \  
cd gst-plugins-base && \  
git checkout $GST_VERSION && \  
meson build --prefix=/usr --libdir=/usr/lib --buildtype=release && \  
ninja -C build -j `nproc` && \  
ninja -C build install && \  
cd .. && \  
rm -rvf /gst-plugins-base  
  
# Fetch and build gst-plugins-good  
RUN git clone -b $GST_VERSION --depth 1
git://anongit.freedesktop.org/git/gstreamer/gst-plugins-good && \  
cd gst-plugins-good && \  
git checkout $GST_VERSION && \  
meson build --prefix=/usr --libdir=/usr/lib --buildtype=release && \  
ninja -C build -j `nproc` && \  
ninja -C build install && \  
cd .. && \  
rm -rvf /gst-plugins-good  
  
# Fetch and build gst-plugins-bad  
RUN git clone -b $GST_VERSION --depth 1
git://anongit.freedesktop.org/git/gstreamer/gst-plugins-bad && \  
cd gst-plugins-bad && \  
git checkout $GST_VERSION && \  
meson build --prefix=/usr --libdir=/usr/lib --buildtype=release && \  
ninja -C build -j `nproc` && \  
ninja -C build install && \  
cd .. && \  
rm -rvf /gst-plugins-bad  
  
# Fetch and build gst-plugins-ugly  
RUN git clone -b $GST_VERSION --depth 1
git://anongit.freedesktop.org/git/gstreamer/gst-plugins-ugly && \  
cd gst-plugins-ugly && \  
git checkout $GST_VERSION && \  
meson build --prefix=/usr --libdir=/usr/lib --buildtype=release && \  
ninja -C build -j `nproc` && \  
ninja -C build install && \  
cd .. && \  
rm -rvf /gst-plugins-ugly  
  
# Fetch and build gst-libav  
RUN git clone -b $GST_VERSION --depth 1
git://anongit.freedesktop.org/git/gstreamer/gst-libav && \  
cd gst-libav && \  
git checkout $GST_VERSION && \  
meson build --prefix=/usr --libdir=/usr/lib --buildtype=release && \  
ninja -C build -j `nproc` && \  
ninja -C build install && \  
cd .. && \  
rm -rvf /gst-libav  
  
# Fetch and build gst-rtsp-server  
RUN git clone -b $GST_VERSION --depth 1
git://anongit.freedesktop.org/git/gstreamer/gst-rtsp-server && \  
cd gst-rtsp-server && \  
git checkout $GST_VERSION && \  
meson build --prefix=/usr --libdir=/usr/lib --buildtype=release && \  
ninja -C build -j `nproc` && \  
ninja -C build install && \  
cd .. && \  
rm -rvf /gst-rtsp-server  
  
# Fetch and build gstreamer-vaapi  
RUN git clone -b $GST_VERSION --depth 1
git://anongit.freedesktop.org/git/gstreamer/gstreamer-vaapi && \  
cd gstreamer-vaapi && \  
git checkout $GST_VERSION && \  
meson build --prefix=/usr --libdir=/usr/lib --buildtype=release && \  
ninja -C build -j `nproc` && \  
ninja -C build install && \  
cd .. && \  
rm -rvf /gstreamer-vaapi  
  
# Fetch and build gst-python  
RUN git clone -b $GST_VERSION --depth 1
git://anongit.freedesktop.org/git/gstreamer/gst-python && \  
cd gst-python && \  
git checkout $GST_VERSION && \  
meson build --prefix=/usr --libdir=/usr/lib --buildtype=release && \  
ninja -C build -j `nproc` && \  
ninja -C build install && \  
cd .. && \  
rm -rvf /gst-python  
  
# Do some cleanup  
RUN DEBIAN_FRONTEND=noninteractive apt-get clean && \  
apt-get autoremove -y  

