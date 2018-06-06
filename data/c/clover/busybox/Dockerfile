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
libgcc1 \  
libc6 \  
libc-bin \  
netbase \  
busybox  
RUN find *.deb | xargs -I % dpkg-deb -x % /rootfs  
  
WORKDIR /rootfs  
COPY environment group gshadow localtime login.defs networks passwd shadow
shells etc/  
RUN mkdir -p dev home root tmp run var/log \  
&& cp usr/share/libc-bin/nsswitch.conf etc/ \  
&& chmod 1777 tmp \  
&& ln -s /run var/run \  
&& ./bin/busybox --list-full | xargs dirname | sort | uniq | xargs mkdir -p \  
&& ./bin/busybox --list-full | xargs -I % ln -s /bin/busybox % \  
&& chmod 0640 etc/shadow \  
&& chmod 0666 \  
etc/group \  
etc/login.defs \  
etc/nsswitch.conf \  
etc/passwd \  
etc/networks \  
&& find \  
etc/*.conf \  
etc/ld.so.conf.d/*.conf \  
etc/bindresvport.blacklist \  
etc/default/nss \  
etc/protocols \  
etc/rpc \  
etc/services \  
| xargs -I % \  
sed -i -r \  
-e 's,[[:space:]]*[#]+.*$,,g' \  
-e '/^$/d' \  
-e 's,[[:space:]]+, ,g' \  
% \  
&& rm -rf \  
sbin/ldconfig* \  
usr/bin/catchsegv \  
usr/bin/getconf \  
usr/bin/getent \  
usr/bin/iconv \  
usr/bin/ldd \  
usr/bin/locale \  
usr/bin/localedef \  
usr/bin/pldd \  
usr/bin/tzselect \  
usr/bin/zdump \  
usr/lib/locale \  
usr/sbin/iconvconfig \  
usr/sbin/zic \  
usr/share  
  
WORKDIR /  
  
  
FROM scratch  
  
ENV LANG=C.UTF-8  
  
COPY --from=build /rootfs /  
  
CMD ["sh"]  

