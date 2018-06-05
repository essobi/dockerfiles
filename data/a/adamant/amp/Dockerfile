FROM frebib/debian-builder as builder  
  
ARG SOCAT_VER=1.7.3.2  
ARG SCREEN_VER=v.4.6.2  
ARG LIBEVENT_VER=2.1.8-stable  
ARG TMUX_VER=2.5  
ARG GLIBC_VER=2.26  
ARG PREFIX=/usr  
  
RUN dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get install -qqy dh-autoreconf libncurses5-dev libsqlite3-0 libgcc1
lib32gcc1 \  
# Glibc Dependencies  
linux-libc-dev:i386 g++-multilib \  
&& mkdir -p /output/${PREFIX}/{bin,lib,lib32}  
  
RUN curl -fL http://www.dest-
unreach.org/socat/download/socat-${SOCAT_VER}.tar.gz | tar xz \  
&& cd socat-${SOCAT_VER} \  
&& ./configure --prefix=${PREFIX} \  
&& make -j "$(nproc)" \  
&& mv ./socat /output/${PREFIX}/bin  
  
RUN curl -fL
http://git.savannah.gnu.org/cgit/screen.git/snapshot/screen-${SCREEN_VER}.tar.gz
| tar xz \  
&& cd screen-${SCREEN_VER}/src/ \  
&& ./autogen.sh \  
&& ./configure --prefix=${PREFIX} \  
&& make -j "$(nproc)" \  
&& mv ./screen /output/${PREFIX}/bin  
  
RUN curl -fL
https://github.com/libevent/libevent/releases/download/release-${LIBEVENT_VER}/libevent-${LIBEVENT_VER}.tar.gz
| tar xz \  
&& cd libevent-${LIBEVENT_VER} \  
&& mkdir build/ \  
&& ./configure --prefix=${PREFIX} \  
&& make -j "$(nproc)" \  
&& make DESTDIR="$(pwd)/build" install \  
&& cp -d ./build/${PREFIX}/lib/*.so* /output${PREFIX}/lib  
  
RUN curl -fL
https://github.com/tmux/tmux/releases/download/${TMUX_VER}/tmux-${TMUX_VER}.tar.gz
| tar xz \  
&& cd tmux-${TMUX_VER}/ \  
&& export LE_DIR="../libevent-${LIBEVENT_VER}/build/usr" \  
&& ./configure CFLAGS="-I$LE_DIR/include" LDFLAGS="-L$LE_DIR/lib"
\--prefix=${PREFIX} \  
&& make -j "$(nproc)" \  
&& mv ./tmux /output/${PREFIX}/bin  
  
WORKDIR /tmp/glibc/build  
  
ARG CC="gcc -m32 -mstackrealign"  
ARG CXX="g++ -m32 -mstackrealign"  
# Download and build glibc from source  
RUN curl -fL https://ftp.gnu.org/gnu/glibc/glibc-${GLIBC_VER}.tar.xz \  
| tar xJ --strip-components=1 -C .. && \  
\  
echo "slibdir=${PREFIX}/lib32" >> configparms && \  
echo "rtlddir=${PREFIX}/lib32" >> configparms && \  
echo "sbindir=${PREFIX}/bin" >> configparms && \  
echo "rootsbindir=${PREFIX}/bin" >> configparms && \  
\  
export CFLAGS="-march=i686 -O2 -pipe -fstack-protector-strong" && \  
export CXXFLAGS="-march=i686 -O2 -pipe -fstack-protector-strong" && \  
\  
../configure \  
\--host=i686-pc-linux-gnu \  
\--prefix=${PREFIX} \  
\--libdir="${PREFIX}/lib32" \  
\--libexecdir="${PREFIX}/lib32" \  
\--with-native-system-header-dir=/usr/include/x86_64-linux-gnu \  
\--enable-add-ons \  
\--enable-obsolete-rpc \  
\--enable-kernel=3.10.0 \  
\--enable-bind-now \  
\--disable-profile \  
\--enable-stackguard-randomization \  
\--enable-stack-protector=strong \  
\--enable-lock-elision \  
\--enable-multi-arch \  
\--disable-werror && \  
make -j "$(nproc)" && \  
make -j "$(nproc)" install_root="$(pwd)/out" install  
  
# Copy glibc libs  
RUN cp -d out/${PREFIX}/lib32/*.so /output/${PREFIX}/lib32 && \  
ln -snv ../lib32/ld-linux.so.2 /output/${PREFIX}/lib/ld-linux.so.2  
  
# Yeah we should probably build these from source, but its part of the debian
image.....  
RUN cp -d /usr/lib32/libgcc_s.so.1 /output${PREFIX}/lib32 \  
&& cp -d /lib/$(gcc -print-multiarch)/libgcc_s.so.1 /output/${PREFIX}/lib \  
&& cp -d /usr/lib/$(gcc -print-multiarch)/libsqlite3.so.0
/output/${PREFIX}/lib \  
&& cp -d /usr/lib/$(gcc -print-multiarch)/libsqlite3.so.0.8.6
/output/${PREFIX}/lib  
  
#================  
FROM adamant/busybox:libressl  
  
COPY \--from=builder /output/ /  
  
RUN addgroup -S amp \  
&& adduser -SDG amp amp \  
&& mkdir -p /home/amp/.ampdata/instances /ampdata \  
&& ln -s /ampdata /home/amp/.ampdata/instances/instance \  
&& chown -R amp:amp /ampdata /home/amp \  
&& (echo '#!/bin/sh'; echo 'exec /bin/sh "$@"') > /usr/bin/bash \  
&& chmod +x /usr/bin/bash \  
&& echo /usr/lib32 > /etc/ld.so.conf \  
&& ldconfig && ldconfig -p  
  
WORKDIR /opt/amp  
  
RUN wget -q https://cubecoders.com/Downloads/ampinstmgr.zip \  
&& unzip ampinstmgr.zip \  
&& rm -rf ampinstmgr.zip \  
&& ln -sfv /opt/amp/ampinstmgr /usr/bin  
  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
  
USER amp  
  
VOLUME /ampdata  
WORKDIR /ampdata  
  
ENTRYPOINT ["/sbin/tini","--"]  
CMD ["/start.sh"]  
  
EXPOSE 8080  

