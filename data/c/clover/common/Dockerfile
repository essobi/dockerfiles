FROM library/ubuntu:bionic AS build  
  
ENV LANG=C.UTF-8  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y \  
software-properties-common \  
apt-utils  
  
RUN mkdir /build /rootfs  
WORKDIR /build  
RUN apt-get download \  
zlib1g \  
libtinfo5 \  
libreadline7 \  
libncurses5 \  
libncursesw5 \  
libssl1.0.0 \  
libssl1.1 \  
libstdc++6 \  
libc-bin \  
tzdata \  
ncurses-base \  
readline-common \  
ca-certificates \  
mime-support  
RUN find *.deb | xargs -I % dpkg-deb -x % /rootfs  
  
WORKDIR /rootfs  
RUN rm -rf \  
etc/ca-certificates \  
etc/default \  
etc/ld.so.* \  
etc/bindresvport.blacklist \  
etc/gai.conf \  
etc/init \  
etc/init.d \  
etc/mailcap.order \  
etc/*/README \  
usr/bin/cautious-launcher \  
usr/bin/compose \  
usr/bin/edit \  
usr/bin/print \  
usr/bin/run-mailcap \  
usr/bin/see \  
usr/lib/mime/packages \  
usr/lib/mime/debian-view \  
usr/bin/catchsegv \  
usr/bin/ldd \  
usr/bin/tzselect \  
usr/sbin/update-ca-certificates \  
usr/sbin/update-mime \  
usr/sbin/tzconfig \  
usr/share/bug \  
usr/share/doc \  
usr/share/gcc-* \  
usr/share/gdb \  
usr/share/info \  
usr/share/libc-bin \  
usr/share/lintian \  
usr/share/man \  
&& mv -f sbin/ldconfig.real sbin/ldconfig \  
&& ln -s /usr/share/zoneinfo/UTC etc/localtime \  
&& find \  
etc/mime.types \  
usr/lib/mime/mailcap \  
usr/share/readline/inputrc \  
| xargs -I % sed -i -r \  
-e 's,^[[:space:]]*[#]+.*$,,g' \  
-e 's,[[:space:]]+, ,g' \  
-e '/^[[:space:]]*$/d' \  
% \  
&& ln -s /usr/lib/mime/mailcap etc/mailcap \  
&& cat usr/share/ca-certificates/mozilla/*.crt > etc/ssl/certs/ca-
certificates.crt  
  
WORKDIR /  
  
  
FROM clover/base  
  
ENV LANG=C.UTF-8  
  
COPY --from=build /rootfs /  

