FROM alpine:3.5  
MAINTAINER Alexandre Flament <alex@al-f.net>  
  
ENV NGHTTP2_VERSION 1.21.0  
ENV SPDYLAY_VERSION 1.4.0  
ENV NGHTTP2_RUNTIME_PACKAGES "libgcc libstdc++ jemalloc libev libxml2 jansson
zlib ca-certificates python"  
ENV NGHTTP2_BUILD_PACKAGES="git curl xz clang clang-dev llvm gcc g++ autoconf
automake make libtool file binutils jemalloc-dev libev-dev libxml2-dev
jansson-dev zlib-dev cmake go"  
COPY *.sh *.txt /build/  
  
RUN apk --no-cache -U add $NGHTTP2_RUNTIME_PACKAGES $NGHTTP2_BUILD_PACKAGES
&&\  
/build/build.sh && \  
apk del $NGHTTP2_BUILD_PACKAGES  

