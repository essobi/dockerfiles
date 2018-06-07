FROM golang:1.9-alpine  
  
ARG VIPS_VERSION=8.5.9  
  
RUN apk update && apk add --no-cache openssl ca-certificates && mkdir -p
${GOPATH}/src && \  
wget -O-
https://github.com/jcupitt/libvips/releases/download/v${VIPS_VERSION}/vips-${VIPS_VERSION}.tar.gz
| tar xzC /tmp && \  
echo "@edge http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories && \  
apk update && apk upgrade && apk add --no-cache --virtual .build-dependencies
\  
build-base docker bash openssh python2@edge py-pip py-setuptools \  
zlib-dev libxml2-dev glib-dev gobject-introspection-dev \  
libjpeg-turbo-dev libexif-dev lcms2-dev fftw-dev giflib-dev libpng-dev \  
libwebp-dev orc-dev tiff-dev poppler-dev librsvg-dev libgsf-dev openexr-dev \  
git glide@edge && \  
pip --no-cache-dir install awscli && \  
cd /tmp/vips-${VIPS_VERSION} && \  
./configure \  
\--disable-static \  
\--disable-dependency-tracking \  
\--without-python && \  
make && \  
make install  

