FROM alpine:3.6  
MAINTAINER Anton Wahyu <mail@anton.web.id>  
  
# install qt build packages #  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& apk update \  
&& apk add gtk+ openssl glib fontconfig bash vim \  
&& apk add --virtual .deps git patch make g++ \  
libc-dev gettext-dev zlib-dev bzip2-dev libffi-dev pcre-dev \  
glib-dev atk-dev expat-dev libpng-dev freetype-dev fontconfig-dev \  
libxau-dev libxdmcp-dev libxcb-dev xf86bigfontproto-dev libx11-dev \  
libxrender-dev pixman-dev libxext-dev cairo-dev perl-dev \  
libxfixes-dev libxdamage-dev graphite2-dev icu-dev harfbuzz-dev \  
libxft-dev pango-dev gtk+-dev libdrm-dev \  
libxxf86vm-dev libxshmfence-dev wayland-dev mesa-dev openssl-dev \  
&& git clone --recursive https://github.com/wkhtmltopdf/wkhtmltopdf.git
/tmp/wkhtmltopdf \  
&& cd /tmp/wkhtmltopdf \  
&& git checkout ccf91a0  
  
COPY conf/* /tmp/wkhtmltopdf/qt/  
  
RUN cd /tmp/wkhtmltopdf/qt && \  
patch -p1 -i qt-musl.patch && \  
patch -p1 -i qt-musl-iconv-no-bom.patch && \  
patch -p1 -i qt-recursive-global-mutex.patch && \  
patch -p1 -i qt-font-pixel-size.patch && \  
patch -p1 -i qt-gcc6.patch && \  
sed -i "s|-O2|$CXXFLAGS|" mkspecs/common/g++.conf && \  
sed -i "/^QMAKE_RPATH/s| -Wl,-rpath,||g" mkspecs/common/g++.conf && \  
sed -i "/^QMAKE_LFLAGS\s/s|+=|+= $LDFLAGS|g" mkspecs/common/g++.conf && \  
CFLAGS=-w CPPFLAGS=-w CXXFLAGS=-w LDFLAGS=-w \  
./configure -confirm-license -opensource \  
-prefix /usr \  
-datadir /usr/share/qt \  
-sysconfdir /etc \  
-plugindir /usr/lib/qt/plugins \  
-importdir /usr/lib/qt/imports \  
-fast \  
-release \  
-static \  
-largefile \  
-glib \  
-graphicssystem raster \  
-qt-zlib \  
-qt-libpng \  
-qt-libmng \  
-qt-libtiff \  
-qt-libjpeg \  
-svg \  
-script \  
-webkit \  
-gtkstyle \  
-xmlpatterns \  
-script \  
-scripttools \  
-openssl-linked \  
-nomake demos \  
-nomake docs \  
-nomake examples \  
-nomake tools \  
-nomake tests \  
-nomake translations \  
-no-qt3support \  
-no-pch \  
-no-icu \  
-no-phonon \  
-no-phonon-backend \  
-no-rpath \  
-no-separate-debug-info \  
-no-dbus \  
-no-opengl \  
-no-openvg && \  
NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) && \  
export MAKEFLAGS=-j${NPROC} && \  
export MAKE_COMMAND="make -j${NPROC}" && \  
make && \  
make install && \  
cd /tmp/wkhtmltopdf && \  
qmake && \  
make && \  
make install && \  
rm -rf /tmp/*  
  
# remove qt build packages #  
RUN apk del .deps \  
&& rm -rf /var/cache/apk/*  

