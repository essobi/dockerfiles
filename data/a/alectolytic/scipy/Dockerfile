FROM alpine:latest  
MAINTAINER Arun Neelicattu <arun.neelicattu@gmail.com>  
  
# Linking of locale.h as xlocale.h  
# This is done to ensure successfull install of python numpy package  
# see https://forum.alpinelinux.org/comment/690#comment-690 for more
information.  
  
RUN apk --update add \--virtual scipy-runtime python py-pip \  
&& apk add \--virtual scipy-build \  
build-base python-dev openblas-dev freetype-dev pkgconfig gfortran \  
&& ln -s /usr/include/locale.h /usr/include/xlocale.h \  
&& pip install --no-cache-dir numpy \  
&& pip install --no-cache-dir matplotlib \  
&& pip install --no-cache-dir scipy \  
&& apk del scipy-build \  
&& apk add \--virtual scipy-runtime \  
freetype libgfortran libgcc libpng libstdc++ musl openblas tcl tk \  
&& rm -rf /var/cache/apk/*  

