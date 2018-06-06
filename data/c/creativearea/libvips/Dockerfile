FROM ubuntu:14.04  
MAINTAINER Florent Bourgeois <florent@creative-area.net>  
  
# let the container know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# build dependencies  
RUN apt-get update && apt-get install -y \  
build-essential \  
autoconf \  
libtool \  
pkg-config \  
curl \  
gettext \  
nasm \  
gtk-doc-tools  
  
# build prefix  
ENV DEST /opt  
  
# common build paths and flags  
ENV PKG_CONFIG_PATH ${PKG_CONFIG_PATH}:${DEST}/lib/pkgconfig  
ENV LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${DEST}/lib  
ENV PATH ${PATH}:${DEST}/bin  
ENV CPPFLAGS -I${DEST}/include  
ENV LDFLAGS -L${DEST}/lib  
ENV CFLAGS -O3  
ENV CXXFLAGS -O3  
  
# zlib  
ENV ZLIB_VERSION 1.2.8  
WORKDIR /tmp  
RUN curl -sOL http://zlib.net/zlib-${ZLIB_VERSION}.tar.xz \  
&& tar xJf zlib-${ZLIB_VERSION}.tar.xz \  
&& cd zlib-${ZLIB_VERSION} \  
&& ./configure --prefix=${DEST} \  
&& make \  
&& make install  
  
# libffi  
ENV LIBFFI_VERSION 3.2.1  
WORKDIR /tmp  
RUN curl -sOL ftp://sourceware.org/pub/libffi/libffi-${LIBFFI_VERSION}.tar.gz
\  
&& tar xzf libffi-${LIBFFI_VERSION}.tar.gz \  
&& cd libffi-${LIBFFI_VERSION} \  
&& ./configure --prefix=${DEST} \--enable-shared --disable-static --disable-
builddir \  
&& make \  
&& make install-strip  
  
# glib  
ENV GLIB_VERSION_MAJOR 2  
ENV GLIB_VERSION_MINOR 49  
ENV GLIB_VERSION_PATCH 4  
ENV GLIB_VERSION
${GLIB_VERSION_MAJOR}.${GLIB_VERSION_MINOR}.${GLIB_VERSION_PATCH}  
WORKDIR /tmp  
RUN curl -sOL
http://ftp.gnome.org/pub/gnome/sources/glib/${GLIB_VERSION_MAJOR}.${GLIB_VERSION_MINOR}/glib-${GLIB_VERSION}.tar.xz
\  
&& tar xJf glib-${GLIB_VERSION}.tar.xz \  
&& cd glib-${GLIB_VERSION} \  
&& ./configure --prefix=${DEST} \--enable-shared --disable-static --with-
pcre=internal \  
&& make \  
&& make install-strip  
  
# libxml2  
ENV LIBXML2_VERSION 2.9.4  
WORKDIR /tmp  
RUN curl -sOL http://xmlsoft.org/sources/libxml2-${LIBXML2_VERSION}.tar.gz \  
&& tar xzf libxml2-${LIBXML2_VERSION}.tar.gz \  
&& cd libxml2-${LIBXML2_VERSION} \  
&& ./configure --prefix=${DEST} \--enable-shared --disable-static --without-
python --without-debug --without-docbook --without-ftp --without-html
--without-legacy --without-pattern --without-push --without-regexps --without-
schemas --without-schematron --with-zlib=${DEST} \  
&& make \  
&& make install-strip  
  
# libgsf  
ENV LIBGSF_VERSION_MAJOR 1  
ENV LIBGSF_VERSION_MINOR 14  
ENV LIBGSF_VERSION_PATCH 39  
ENV LIBGSF_VERSION
${LIBGSF_VERSION_MAJOR}.${LIBGSF_VERSION_MINOR}.${LIBGSF_VERSION_PATCH}  
WORKDIR /tmp  
RUN curl -sOL
http://ftp.gnome.org/pub/gnome/sources/libgsf/${LIBGSF_VERSION_MAJOR}.${LIBGSF_VERSION_MINOR}/libgsf-${LIBGSF_VERSION}.tar.xz
\  
&& tar xJf libgsf-${LIBGSF_VERSION}.tar.xz \  
&& cd libgsf-${LIBGSF_VERSION} \  
&& ./configure --prefix=${DEST} \--enable-shared --disable-static \  
&& make \  
&& make install-strip  
  
# libexif  
ENV LIBEXIF_VERSION 0.6.21  
WORKDIR /tmp  
RUN curl -sOL
http://prdownloads.sourceforge.net/libexif/libexif-${LIBEXIF_VERSION}.tar.bz2
\  
&& tar xjf libexif-${LIBEXIF_VERSION}.tar.bz2 \  
&& cd libexif-${LIBEXIF_VERSION} \  
&& ./configure --prefix=${DEST} \--enable-shared --disable-static \  
&& make \  
&& make install-strip  
  
# lcms2  
ENV LCMS2_VERSION 2.8  
WORKDIR /tmp  
RUN curl -sOL
http://prdownloads.sourceforge.net/lcms/lcms2-${LCMS2_VERSION}.tar.gz \  
&& tar xzf lcms2-${LCMS2_VERSION}.tar.gz \  
&& cd lcms2-${LCMS2_VERSION} \  
&& ./configure --prefix=${DEST} \--enable-shared --disable-static \  
&& make \  
&& make install-strip  
  
# libjpeg-turbo  
ENV LIBJPEG_TURBO_VERSION 1.5.0  
WORKDIR /tmp  
RUN curl -sOL http://prdownloads.sourceforge.net/libjpeg-turbo/libjpeg-
turbo-${LIBJPEG_TURBO_VERSION}.tar.gz \  
&& tar xzf libjpeg-turbo-${LIBJPEG_TURBO_VERSION}.tar.gz \  
&& cd libjpeg-turbo-${LIBJPEG_TURBO_VERSION} \  
&& ./configure --prefix=${DEST} \--enable-shared --disable-static --with-jpeg8
--without-turbojpeg \  
&& make \  
&& make install-strip  
  
# libtiff  
ENV LIBTIFF_VERSION 4.0.6  
WORKDIR /tmp  
RUN curl -sOL http://download.osgeo.org/libtiff/tiff-${LIBTIFF_VERSION}.tar.gz
\  
&& tar xzf tiff-${LIBTIFF_VERSION}.tar.gz \  
&& cd tiff-${LIBTIFF_VERSION} \  
&& ./configure --prefix=${DEST} \--enable-shared --disable-static --disable-
mdi --disable-cxx \  
&& make \  
&& make install-strip  
  
# libpng  
ENV LIBPNG_VERSION 1.6.25  
WORKDIR /tmp  
RUN curl -sOL
http://prdownloads.sourceforge.net/libpng/libpng-${LIBPNG_VERSION}.tar.gz \  
&& tar xzf libpng-${LIBPNG_VERSION}.tar.gz \  
&& cd libpng-${LIBPNG_VERSION} \  
&& ./configure --prefix=${DEST} \--enable-shared --disable-static \  
&& make \  
&& make install-strip  
  
# libgif  
ENV GIFLIB_VERSION 5.1.4  
WORKDIR /tmp  
RUN curl -sOL
http://prdownloads.sourceforge.net/giflib/giflib-${GIFLIB_VERSION}.tar.gz \  
&& tar xzf giflib-${GIFLIB_VERSION}.tar.gz \  
&& cd giflib-${GIFLIB_VERSION} \  
&& ./configure --prefix=${DEST} \--enable-shared --disable-static \  
&& make \  
&& make install-strip  
  
# libwebp  
ENV LIBWEBP_VERSION 0.5.1  
WORKDIR /tmp  
RUN curl -sOL
https://storage.googleapis.com/downloads.webmproject.org/releases/webp/libwebp-${LIBWEBP_VERSION}.tar.gz
\  
&& tar xzf libwebp-${LIBWEBP_VERSION}.tar.gz \  
&& cd libwebp-${LIBWEBP_VERSION} \  
&& ./configure --prefix=${DEST} \--enable-shared --disable-static --disable-
neon \  
&& make \  
&& make install-strip  
  
# orc  
ENV ORC_VERSION 0.4.25  
WORKDIR /tmp  
RUN curl -sOL
http://gstreamer.freedesktop.org/data/src/orc/orc-${ORC_VERSION}.tar.xz \  
&& tar xJf orc-${ORC_VERSION}.tar.xz \  
&& cd orc-${ORC_VERSION} \  
&& ./configure --prefix=${DEST} \--enable-shared --disable-static \  
&& make \  
&& make install-strip  
  
# gdk-pixbuf  
ENV GDKPIXBUFF_VERSION_MAJOR 2  
ENV GDKPIXBUFF_VERSION_MINOR 35  
ENV GDKPIXBUFF_VERSION_PATCH 2  
ENV GDKPIXBUFF_VERSION
${GDKPIXBUFF_VERSION_MAJOR}.${GDKPIXBUFF_VERSION_MINOR}.${GDKPIXBUFF_VERSION_PATCH}  
WORKDIR /tmp  
RUN curl -sOL http://ftp.gnome.org/pub/gnome/sources/gdk-
pixbuf/${GDKPIXBUFF_VERSION_MAJOR}.${GDKPIXBUFF_VERSION_MINOR}/gdk-
pixbuf-${GDKPIXBUFF_VERSION}.tar.xz \  
&& tar xJf gdk-pixbuf-${GDKPIXBUFF_VERSION}.tar.xz \  
&& cd gdk-pixbuf-${GDKPIXBUFF_VERSION} \  
&& ./configure --prefix=${DEST} \--enable-shared --disable-static --disable-
introspection --disable-modules --disable-gio-sniffing --without-libpng
--without-libjpeg --without-libtiff --without-gdiplus --with-included-loaders=
\  
&& make \  
&& make install-strip  
  
# libcroco  
ENV LIBCROCO_VERSION_MAJOR 0  
ENV LIBCROCO_VERSION_MINOR 6  
ENV LIBCROCO_VERSION_PATCH 11  
ENV LIBCROCO_VERSION
${LIBCROCO_VERSION_MAJOR}.${LIBCROCO_VERSION_MINOR}.${LIBCROCO_VERSION_PATCH}  
WORKDIR /tmp  
RUN curl -sOL
http://ftp.gnome.org/pub/gnome/sources/libcroco/${LIBCROCO_VERSION_MAJOR}.${LIBCROCO_VERSION_MINOR}/libcroco-${LIBCROCO_VERSION}.tar.xz
\  
&& tar xJf libcroco-${LIBCROCO_VERSION}.tar.xz \  
&& cd libcroco-${LIBCROCO_VERSION} \  
&& ./configure --prefix=${DEST} \--enable-shared --disable-static \  
&& make \  
&& make install-strip  
  
# freetype  
ENV FREETYPE_VERSION 2.6.5  
WORKDIR /tmp  
RUN curl -sOL
http://download.savannah.gnu.org/releases/freetype/freetype-${FREETYPE_VERSION}.tar.gz
\  
&& tar xzf freetype-${FREETYPE_VERSION}.tar.gz \  
&& cd freetype-${FREETYPE_VERSION} \  
&& ./configure --prefix=${DEST} \--enable-shared --disable-static \  
&& make \  
&& make install  
  
# fontconfig  
ENV FONTCONFIG_VERSION 2.12.0  
WORKDIR /tmp  
RUN curl -sOL
https://www.freedesktop.org/software/fontconfig/release/fontconfig-${FONTCONFIG_VERSION}.tar.bz2
\  
&& tar xjf fontconfig-${FONTCONFIG_VERSION}.tar.bz2 \  
&& cd fontconfig-${FONTCONFIG_VERSION} \  
&& ./configure --prefix=${DEST} \--enable-shared --disable-static --enable-
libxml2 \  
&& make \  
&& make install-strip  
  
# harfbuzz  
ENV HARFBUZZ_VERSION 1.3.0  
WORKDIR /tmp  
RUN curl -sOL
https://www.freedesktop.org/software/harfbuzz/release/harfbuzz-${HARFBUZZ_VERSION}.tar.bz2
\  
&& tar xjf harfbuzz-${HARFBUZZ_VERSION}.tar.bz2 \  
&& cd harfbuzz-${HARFBUZZ_VERSION} \  
&& ./configure --prefix=${DEST} \--enable-shared --disable-static \  
&& make \  
&& make install-strip  
  
# pixman  
ENV PIXMAN_VERSION 0.34.0  
WORKDIR /tmp  
RUN curl -sOL
http://cairographics.org/releases/pixman-${PIXMAN_VERSION}.tar.gz \  
&& tar xzf pixman-${PIXMAN_VERSION}.tar.gz \  
&& cd pixman-${PIXMAN_VERSION} \  
&& ./configure --prefix=${DEST} \--enable-shared --disable-static --disable-
libpng --disable-arm-iwmmxt \  
&& make \  
&& make install-strip  
  
# cairo  
ENV CAIRO_VERSION 1.14.6  
WORKDIR /tmp  
RUN curl -sOL http://cairographics.org/releases/cairo-${CAIRO_VERSION}.tar.xz
\  
&& tar xJf cairo-${CAIRO_VERSION}.tar.xz \  
&& cd cairo-${CAIRO_VERSION} \  
&& ./configure --prefix=${DEST} \--enable-shared --disable-static --disable-
xlib --disable-xcb --disable-quartz --disable-win32 --disable-egl --disable-
glx --disable-wgl --disable-script --disable-ps --disable-gobject --disable-
trace --disable-interpreter \  
&& make \  
&& make install-strip  
  
# pango  
ENV PANGO_VERSION_MAJOR 1  
ENV PANGO_VERSION_MINOR 40  
ENV PANGO_VERSION_PATCH 1  
ENV PANGO_VERSION
${PANGO_VERSION_MAJOR}.${PANGO_VERSION_MINOR}.${PANGO_VERSION_PATCH}  
WORKDIR /tmp  
RUN curl -sOL
http://ftp.gnome.org/pub/gnome/sources/pango/${PANGO_VERSION_MAJOR}.${PANGO_VERSION_MINOR}/pango-${PANGO_VERSION}.tar.xz
\  
&& tar xJf pango-${PANGO_VERSION}.tar.xz \  
&& cd pango-${PANGO_VERSION} \  
&& ./configure --prefix=${DEST} \--enable-shared --disable-static \  
&& make \  
&& make install-strip  
  
#librsvg  
ENV LIBRSVG_VERSION_MAJOR 2  
ENV LIBRSVG_VERSION_MINOR 40  
ENV LIBRSVG_VERSION_PATCH 16  
ENV LIBRSVG_VERSION
${LIBRSVG_VERSION_MAJOR}.${LIBRSVG_VERSION_MINOR}.${LIBRSVG_VERSION_PATCH}  
WORKDIR /tmp  
RUN curl -sOL
http://ftp.gnome.org/pub/gnome/sources/librsvg/${LIBRSVG_VERSION_MAJOR}.${LIBRSVG_VERSION_MINOR}/librsvg-${LIBRSVG_VERSION}.tar.xz
\  
&& tar xJf librsvg-${LIBRSVG_VERSION}.tar.xz \  
&& cd librsvg-${LIBRSVG_VERSION} \  
&& ./configure --prefix=${DEST} \--enable-shared --disable-static --disable-
introspection --disable-tools --disable-pixbuf-loader \  
&& make \  
&& make install-strip  
  
# libvips  
WORKDIR /tmp  
ENV LIBVIPS_VERSION_MAJOR 8  
ENV LIBVIPS_VERSION_MINOR 3  
ENV LIBVIPS_VERSION_PATCH 3  
ENV LIBVIPS_VERSION
${LIBVIPS_VERSION_MAJOR}.${LIBVIPS_VERSION_MINOR}.${LIBVIPS_VERSION_PATCH}  
RUN curl -sOL
http://www.vips.ecs.soton.ac.uk/supported/${LIBVIPS_VERSION_MAJOR}.${LIBVIPS_VERSION_MINOR}/vips-${LIBVIPS_VERSION}.tar.gz
\  
&& tar zxf vips-${LIBVIPS_VERSION}.tar.gz \  
&& cd vips-${LIBVIPS_VERSION} \  
&& ./configure --prefix=${DEST} \--without-python --without-fftw --without-
magick --without-pangoft2 --without-ppm --without-analyze --without-radiance
--without-openslide --with-zip-includes=${DEST}/include --with-zip-
libraries=${DEST}/lib --with-jpeg-includes=${DEST}/include --with-jpeg-
libraries=${DEST}/lib \  
&& make \  
&& make install  
  
WORKDIR /  
  
# cleanup  
RUN apt-get remove -y build-essential autoconf libtool pkg-config curl gettext
nasm gtk-doc-tools && \  
apt-get autoremove -y && \  
apt-get autoclean && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

