FROM frolvlad/alpine-glibc:alpine-3.3  
MAINTAINER Marcus Griep <marcus@griep.us>  
  
ENV MONO_VERSION 4.2.2.30-2  
  
RUN apk add \--no-cache \--virtual=build-dependencies wget ca-certificates tar
xz && \  
wget \--progress=dot:mega
https://archive.archlinux.org/packages/m/mono/mono-$MONO_VERSION-x86_64.pkg.tar.xz
-O /tmp/mono.pkg.tar.xz && \  
tar -xJf /tmp/mono.pkg.tar.xz && \  
mozroots \--import \--ask-remove && \  
apk del build-dependencies && \  
rm /tmp/*  

