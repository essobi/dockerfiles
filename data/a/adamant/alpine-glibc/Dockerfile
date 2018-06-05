FROM alpine:3.5  
MAINTAINER Adam Dodman <adam.dodman@gmx.com>  
  
ENV DESTDIR="/glibc"  
ENV GLIBC_LIBRARY_PATH="$DESTDIR/lib" DEBS="libc6 libgcc1 libstdc++6"  
ENV GLIBC_LD_LINUX_SO="$GLIBC_LIBRARY_PATH/ld-linux-x86-64.so.2"  
  
WORKDIR /tmp  
  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& apk add --no-cache xz binutils patchelf \  
&& wget http://ftp.debian.org/debian/pool/main/g/glibc/libc6_2.24-9_amd64.deb
\  
&& wget
http://ftp.debian.org/debian/pool/main/g/gcc-4.9/libgcc1_4.9.2-10_amd64.deb \  
&& wget
http://ftp.debian.org/debian/pool/main/g/gcc-4.9/libstdc++6_4.9.2-10_amd64.deb
\  
  
&& for pkg in $DEBS; do \  
mkdir $pkg; \  
cd $pkg; \  
ar x ../$pkg*.deb; \  
tar -xf data.tar.*; \  
cd ..; \  
done \  
  
&& mkdir -p $GLIBC_LIBRARY_PATH \  
  
&& mv libc6/lib/x86_64-linux-gnu/* $GLIBC_LIBRARY_PATH \  
&& mv libgcc1/lib/x86_64-linux-gnu/* $GLIBC_LIBRARY_PATH \  
&& mv libstdc++6/usr/lib/x86_64-linux-gnu/* $GLIBC_LIBRARY_PATH \  
&& apk del --no-cache xz binutils \  
&& rm -rf /tmp/*  
  
WORKDIR $DESTDIR  

