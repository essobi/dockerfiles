FROM alpine:latest AS alpine-packages  
  
RUN apk add --update --no-cache --virtual .build-dependencies \  
autoconf \  
automake \  
build-base \  
curl \  
expat-dev \  
glib-dev \  
libexif \  
libtool \  
nasm  
  
WORKDIR /tmp  
  
# zlib  
RUN \  
ZLIB_VERSION=1.2.11 \  
&& curl -L -O https://zlib.net/zlib-$ZLIB_VERSION.tar.gz \  
&& tar zxf zlib-$ZLIB_VERSION.tar.gz \  
&& cd zlib-$ZLIB_VERSION \  
&& ./configure --prefix /usr/local && make && make install  
  
# bzip2  
RUN \  
BZIP2_VERSION=1.0.6 \  
&& curl -L -O http://www.bzip.org/$BZIP2_VERSION/bzip2-$BZIP2_VERSION.tar.gz \  
&& tar zxf bzip2-$BZIP2_VERSION.tar.gz \  
&& cd bzip2-$BZIP2_VERSION \  
&& make PREFIX=/usr/local && make install  
  
# libjpeg  
RUN \  
LIBJPEG_TURBO_VERSION=1.5.3 \  
&& curl -L -O https://downloads.sourceforge.net/libjpeg-turbo/libjpeg-
turbo-$LIBJPEG_TURBO_VERSION.tar.gz \  
&& tar zxf libjpeg-turbo-$LIBJPEG_TURBO_VERSION.tar.gz \  
&& cd libjpeg-turbo-$LIBJPEG_TURBO_VERSION \  
&& ./configure --prefix /usr/local \--with-jpeg8 && make && make install  
  
# libpng  
RUN \  
LIBPNG_VERSION=1.6.34 \  
&& curl -L -O
https://download.sourceforge.net/libpng/libpng-$LIBPNG_VERSION.tar.gz \  
&& tar zxf libpng-$LIBPNG_VERSION.tar.gz \  
&& cd libpng-$LIBPNG_VERSION \  
&& ./configure --prefix /usr/local && make && make install  
  
# libwebp  
RUN \  
LIBWEBP_VERSION=1.0.0 \  
&& curl -L -O
https://storage.googleapis.com/downloads.webmproject.org/releases/webp/libwebp-$LIBWEBP_VERSION.tar.gz
\  
&& tar zxf libwebp-$LIBWEBP_VERSION.tar.gz \  
&& cd libwebp-$LIBWEBP_VERSION \  
&& ./configure --prefix /usr/local \--enable-libwebpmux --enable-libwebpdemux
&& make && make install  
  
# advancecomp  
# https://github.com/amadvance/advancecomp/releases  
RUN \  
ADVANCECOMP_VERSION=2.1 \  
&& curl -L -O
https://github.com/amadvance/advancecomp/releases/download/v$ADVANCECOMP_VERSION/advancecomp-$ADVANCECOMP_VERSION.tar.gz
\  
&& tar zxf advancecomp-$ADVANCECOMP_VERSION.tar.gz \  
&& cd advancecomp-$ADVANCECOMP_VERSION \  
&& ./configure --prefix /usr/local && make && make install  
  
# gifsicle  
# https://github.com/kohler/gifsicle/releases  
RUN \  
GIFSICLE_VERSION=1.91 \  
&& curl -L -O https://lcdf.org/gifsicle/gifsicle-$GIFSICLE_VERSION.tar.gz \  
&& tar zxf gifsicle-$GIFSICLE_VERSION.tar.gz \  
&& cd gifsicle-$GIFSICLE_VERSION \  
&& autoreconf -i && ./configure --prefix /usr/local && make && make install  
  
# jhead  
# https://github.com/danielgtaylor/jpeg-archive/releases  
RUN \  
JHEAD_VERSION=3.00 \  
&& curl -O http://www.sentex.net/~mwandel/jhead/jhead-$JHEAD_VERSION.tar.gz \  
&& tar zxf jhead-$JHEAD_VERSION.tar.gz \  
&& cd jhead-$JHEAD_VERSION \  
&& make && make install  
  
# jpeg-recompress (from jpeg-archive along with mozjpeg dependency)  
# https://sourceforge.net/projects/optipng/files/OptiPNG/  
RUN \  
MOZJPEG_VERSION=3.3.1 \  
&& curl -L -O
https://github.com/mozilla/mozjpeg/archive/v$MOZJPEG_VERSION.tar.gz \  
&& tar zxf v$MOZJPEG_VERSION.tar.gz \  
&& cd mozjpeg-$MOZJPEG_VERSION \  
&& autoreconf -fiv && ./configure && make && make install  
RUN \  
JPEGARCHIVE_VERSION=2.1.1 \  
&& curl -L -O https://github.com/danielgtaylor/jpeg-
archive/archive/$JPEGARCHIVE_VERSION.tar.gz \  
&& tar zxf $JPEGARCHIVE_VERSION.tar.gz \  
&& cd jpeg-archive-$JPEGARCHIVE_VERSION \  
&& make && make install  
  
# jpegoptim  
# http://www.kokkonen.net/tjko/projects.html#jpegoptim  
RUN \  
JPEGOPTIM_VERSION=1.4.6 \  
&& curl -O
http://www.kokkonen.net/tjko/src/jpegoptim-$JPEGOPTIM_VERSION.tar.gz \  
&& tar zxf jpegoptim-$JPEGOPTIM_VERSION.tar.gz \  
&& cd jpegoptim-$JPEGOPTIM_VERSION \  
&& ./configure --prefix /usr/local && make && make install  
  
# jpegtran (from Independent JPEG Group)  
# http://www.ijg.org/  
RUN \  
IJG_VERSION=9c \  
&& curl -O http://www.ijg.org/files/jpegsrc.v$IJG_VERSION.tar.gz \  
&& tar zxf jpegsrc.v$IJG_VERSION.tar.gz \  
&& cd jpeg-$IJG_VERSION \  
&& ./configure --prefix /usr/local && make && make install  
  
# optipng  
# https://sourceforge.net/projects/pmt/files/pngcrush/  
RUN \  
OPTIPNG_VERSION=0.7.7 \  
&& curl -L -O
http://downloads.sourceforge.net/project/optipng/OptiPNG/optipng-$OPTIPNG_VERSION/optipng-$OPTIPNG_VERSION.tar.gz
\  
&& tar zxf optipng-$OPTIPNG_VERSION.tar.gz \  
&& cd optipng-$OPTIPNG_VERSION \  
&& ./configure && make && make install  
  
# pngcrush  
RUN \  
PNGCRUSH_VERSION=1.8.13 \  
&& curl -L -O
http://downloads.sourceforge.net/project/pmt/pngcrush/$PNGCRUSH_VERSION/pngcrush-$PNGCRUSH_VERSION.tar.gz
\  
&& tar zxf pngcrush-$PNGCRUSH_VERSION.tar.gz \  
&& cd pngcrush-$PNGCRUSH_VERSION \  
&& make && cp -f pngcrush /usr/local/bin  
  
# pngout (binary distrib)  
RUN \  
PNGOUT_VERSION=20150319 \  
&& curl -O http://static.jonof.id.au/dl/kenutils/pngout-$PNGOUT_VERSION-linux-
static.tar.gz \  
&& tar zxf pngout-$PNGOUT_VERSION-linux-static.tar.gz \  
&& cd pngout-$PNGOUT_VERSION-linux-static \  
&& cp -f x86_64/pngout-static /usr/local/bin/pngout  
  
# pngquant  
# https://github.com/pornel/pngquant/releases  
# https://github.com/ImageOptim/libimagequant/releases  
RUN \  
PNGQUANT_VERSION=2.11.7 \  
LIBIMAGEQUANT_VERSION=2.11.10 \  
&& curl -L -O
https://github.com/ImageOptim/libimagequant/archive/$LIBIMAGEQUANT_VERSION.tar.gz
\  
&& tar xzf $LIBIMAGEQUANT_VERSION.tar.gz \  
&& curl -L -O
https://github.com/pornel/pngquant/archive/$PNGQUANT_VERSION.tar.gz \  
&& tar xzf $PNGQUANT_VERSION.tar.gz \  
&& mv libimagequant-$LIBIMAGEQUANT_VERSION/* pngquant-$PNGQUANT_VERSION/lib/ \  
&& cd pngquant-$PNGQUANT_VERSION \  
&& ./configure --prefix /usr/local && make && make install  
  
# mediainfo  
RUN \  
ZENLIB_VERSION=0.4.37 \  
&& curl -L -O
https://github.com/MediaArea/ZenLib/archive/v$ZENLIB_VERSION.tar.gz \  
&& tar zxf v$ZENLIB_VERSION.tar.gz \  
&& cd ZenLib-$ZENLIB_VERSION/Project/GNU/Library \  
&& ./autogen.sh && ./configure --prefix /usr/local \--enable-static && make &&
make install  
RUN \  
MEDIAINFO_VERSION=18.03.1 \  
&& curl -L -O
https://github.com/MediaArea/MediaInfoLib/archive/v$MEDIAINFO_VERSION.tar.gz \  
&& tar zxf v$MEDIAINFO_VERSION.tar.gz \  
&& cd MediaInfoLib-$MEDIAINFO_VERSION/Project/GNU/Library \  
&& ./autogen.sh && ./configure --prefix /usr/local \--enable-static && make &&
make install \  
&& curl -L -O
https://github.com/MediaArea/MediaInfo/archive/v$MEDIAINFO_VERSION.tar.gz \  
&& tar zxf v$MEDIAINFO_VERSION.tar.gz \  
&& cd MediaInfo-$MEDIAINFO_VERSION/Project/GNU/CLI \  
&& ./autogen.sh && ./configure --prefix /usr/local \--enable-static --enable-
staticlibs && make && make install  
  
# imagemagick  
RUN \  
curl -L -O https://www.imagemagick.org/download/ImageMagick.tar.gz \  
&& tar zxf ImageMagick.tar.gz \  
&& cd ImageMagick-* \  
&& ./configure --prefix /usr/local \--enable-shared=no --with-modules=no &&
make && make install  
  
# vips  
RUN \  
VIPS_VERSION=8.6.3 \  
&& curl -L -O
https://github.com/jcupitt/libvips/releases/download/v$VIPS_VERSION/vips-$VIPS_VERSION.tar.gz
\  
&& tar zxf vips-$VIPS_VERSION.tar.gz \  
&& cd vips-$VIPS_VERSION \  
&& ./configure --prefix /usr/local \--with-modules=no --without-magick && make
&& make install  
  
# wkhtmltopdf  
RUN \  
WKHTMLTOX_VERSION=0.12.4 \  
&& curl -L -o wkhtmltox.tar.xz
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/$WKHTMLTOX_VERSION/wkhtmltox-${WKHTMLTOX_VERSION}_linux-
generic-amd64.tar.xz \  
&& tar xf wkhtmltox.tar.xz \  
&& cp wkhtmltox/bin/wkhtmltopdf /usr/local/bin \  
&& cp wkhtmltox/bin/wkhtmltoimage /usr/local/bin  
  
RUN apk del .build-dependencies  
  
FROM starefossen/ruby-node:alpine  
  
RUN apk add --no-cache \  
libexif \  
libgomp \  
libtool  
  
COPY \--from=alpine-packages /usr/local/bin /usr/local/bin  
COPY \--from=alpine-packages /usr/local/lib /usr/local/lib  

