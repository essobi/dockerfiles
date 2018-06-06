FROM alpine:3.5  
  
LABEL maintainer="Dirk Lüth <info@qoopido.com>" \  
org.label-schema.docker.dockerfile="/Dockerfile" \  
org.label-schema.name="Qoopido Docker Converter (Alpine)" \  
org.label-schema.url="https://github.com/dlueth/docker.alpine.converter" \  
org.label-schema.vcs-
url="https://github.com/dlueth/docker.alpine.converter.git"  
# Set environment variables  
ENV IMAGEMAGICK_VERSION "7.0.5-4"  
ENV CFLAGS "-Os -fomit-frame-pointer -fPIE -fstack-protector-all
-D_FORTIFY_SOURCE=2"  
ENV CPPFLAGS "${CFLAGS}"  
ENV CXXFLAGS "${CFLAGS}"  
ENV LDFLAGS "-Wl,-z,now -Wl,-z,relro,--as-needed"  
# Copy files & directories  
COPY entrypoint.sh /entrypoint.sh  
  
# Alter permissions  
RUN chmod +x /entrypoint.sh  
  
# create user and group  
RUN adduser -s /bin/sh -g imagemagick -D imagemagick \  
&& exit 0 ; exit 1  
# Compile & install ImageMagick  
# glib  
# glib-dev  
RUN apk update \  
&& apk upgrade \  
&& apk add --update --no-cache libtool libgomp ghostscript-fonts zlib libpng
libjpeg-turbo freetype fontconfig perl ghostscript libwebp tiff lcms2 libxml2
fftw \  
&& apk add --update --no-cache --virtual .temporary build-base curl xz zlib-
dev libpng-dev libjpeg-turbo-dev freetype-dev fontconfig-dev perl-dev
ghostscript-dev libwebp-dev tiff-dev lcms2-dev libxml2-dev fftw-dev \  
# Install ImageMagick  
&& mkdir -p /tmp/ImageMagick \  
&& curl -fsSL -o /tmp/ImageMagick/ImageMagick.tar.gz
https://gitlab.com/ImageMagick/ImageMagick/repository/archive.tar.gz?ref=${IMAGEMAGICK_VERSION}
\  
&& tar -C /tmp/ImageMagick -xvzf /tmp/ImageMagick/ImageMagick.tar.gz \  
&& cd $(find /tmp/ImageMagick/* -maxdepth 0 -type d -name "ImageMagick*") \  
&& ./configure \  
\--build=${CBUILD} \  
\--host=${CHOST} \  
\--prefix=/usr \  
\--sysconfdir=/etc \  
\--mandir=/usr/share/man \  
\--infodir=/usr/share/info \  
\--localstatedir=/var \  
\--enable-shared \  
\--disable-static \  
\--disable-hdri \  
\--with-quantum-depth=8 \  
\--with-gs-font-dir=/usr/share/fonts/Type1 \  
\--with-gslib \  
\--with-fontconfig \  
\--with-freetype \  
\--with-xml \  
\--with-perl \  
\--without-x \  
\--with-modules \  
\--with-tiff \  
\--with-jpeg \  
\--with-png \  
&& make -j1 \  
&& make install \  
&& ldconfig /usr/local/lib \  
&& convert -version \  
# Cleanup  
&& apk del .temporary \  
&& rm -rf /var/cache/apk/* /tmp/*  
  
# Settings  
ENTRYPOINT [ "/entrypoint.sh" ]  

