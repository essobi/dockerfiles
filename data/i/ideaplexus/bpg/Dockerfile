FROM alpine:latest AS build  
  
ARG LIBBPG_VERSION=0.9.8  
ENV LIBBPG_VERSION=$LIBBPG_VERSION  
  
RUN set -e \  
&& cd /tmp \  
&& mkdir -p /tmp/build \  
&& wget https://bellard.org/bpg/libbpg-${LIBBPG_VERSION}.tar.gz \  
&& tar xzf libbpg-${LIBBPG_VERSION}.tar.gz -C /tmp/build \--strip-components=1
\  
&& apk add \--update --repository http://dl-
cdn.alpinelinux.org/alpine/edge/testing/ --allow-untrusted build-base cmake
emscripten libjpeg-turbo-dev libpng-dev sdl-dev sdl_image-dev yasm \  
&& cd /tmp/build \  
&& sed -i -e 's/#USE_EMCC=y/USE_EMCC=y/g' Makefile \  
&& make \  
&& mkdir -p /bpg/bin /bpg/js /bpg/data \  
&& mv bpgenc bpgdec bpgview /bpg/bin/ \  
&& mv bpgdec.js bpgdec8.js bpgdec8a.js /bpg/js/  
  
FROM alpine:latest  
  
COPY \--from=build /bpg /bpg  
  
RUN set -e \  
&& apk add \--no-cache libjpeg-turbo libpng libstdc++ \  
&& addgroup -g 1000 -S bpg \  
&& adduser -u 1000 -S bpg -G bpg \  
&& ln -s /bpg/bin/* /usr/local/bin/ \  
&& chown -R bpg:bpg /bpg  
  
USER bpg  
  
WORKDIR /bpg/data

