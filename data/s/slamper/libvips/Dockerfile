FROM alpine:edge  
  
# Install dependencies  
RUN apk --update add --no-cache --virtual build-deps \  
gcc g++ make libc-dev \  
curl \  
automake \  
libtool \  
tar \  
gettext \  
git  
RUN apk --update add --no-cache --virtual dev-deps \  
glib-dev \  
libpng-dev \  
libwebp-dev \  
libexif-dev \  
libxml2-dev \  
libjpeg-turbo-dev \  
expat-dev \  
orc-dev \  
giflib-dev \  
librsvg-dev \  
lcms2-dev \  
openexr-dev \  
tiff-dev  
RUN apk --update add --no-cache --virtual run-deps \  
glib \  
libpng \  
libwebp \  
libexif \  
libxml2 \  
giflib \  
librsvg \  
libjpeg-turbo \  
ca-certificates \  
orc \  
lcms2 \  
openexr \  
tiff  
  
WORKDIR /tmp  
ENV LIBVIPS_URL
https://github.com/jcupitt/libvips/releases/download/v8.6.0-alpha4/vips-8.6.0-3.tar.gz  
ENV LIBVIPS_FILE vips-8.6.0-3.tar.gz  
ENV LIBVIPS_VERSION 8.6.0  
# Build libvips  
RUN curl -O -L ${LIBVIPS_URL} && \  
tar zvxf ${LIBVIPS_FILE} && \  
cd vips-${LIBVIPS_VERSION} && \  
./configure --without-python --without-gsf && \  
make && \  
make install  
ENV CPATH /usr/local/include  
ENV LIBRARY_PATH /usr/local/lib  
  
# Cleanup image  
RUN apk del build-deps dev-deps  
  
# Patch glibc  
RUN mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-
linux-x86-64.so.2  
  
# Generate working dir  
RUN mkdir /data  
WORKDIR /data  

