# Gource bundled with FFmpeg  
#  
# VERSION 0.47  
FROM alpine:3.7  
  
ARG VCS_REF  
ARG BUILD_DATE  
  
LABEL maintainer="James Brink, brink.james@gmail.com" \  
decription="Gource 0.47 bundled with FFmpeg 3.4" \  
version="0.47" \  
org.label-schema.name="gource" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/jamesbrink/docker-gource" \  
org.label-schema.schema-version="1.0.0-rc1"  
# Install all needed deps and compile the mesa llvmpipe driver from source.  
RUN set -xe; \  
apk --update add \--no-cache --virtual .runtime-deps gource xvfb llvm5-libs
ffmpeg; \  
apk add \--no-cache --virtual .build-deps llvm-dev build-base zlib-dev glproto
xorg-server-dev python-dev; \  
mkdir -p /var/tmp/build; \  
cd /var/tmp/build; \  
wget "https://mesa.freedesktop.org/archive/mesa-18.0.0-rc5.tar.gz"; \  
tar xfv mesa-18.0.0-rc5.tar.gz; \  
rm mesa-18.0.0-rc5.tar.gz; \  
cd mesa-18.0.0-rc5; \  
./configure \--enable-glx=gallium-xlib \--with-gallium-drivers=swrast
--disable-dri --disable-gbm --disable-egl \--prefix=/usr/local; \  
make; \  
make install; \  
cd .. ; \  
rm -rf mesa-18.0.0-rc5; \  
apk del .build-deps;  
  
COPY ./entrypoint.sh /usr/local/bin/entrypoint.sh  
  
ENV XVFB_WHD="3840x2160x24"\  
DISPLAY=":99"  
  
CMD ["/usr/local/bin/entrypoint.sh"]  

