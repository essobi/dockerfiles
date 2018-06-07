FROM alpine:3.2  
MAINTAINER Reza Farrahi M <imriss@yahoo.com>  
  
RUN apk --update add wget build-base python python-dev git ca-certificates zip  
RUN apk --update add --virtual build-deps gcc g++ make libc-dev curl automake
libtool tar gettext  
RUN apk --update add --virtual dev-deps glib-dev libpng-dev libwebp-dev
libexif-dev libxml2-dev libjpeg-turbo-dev  
RUN apk --update add --virtual run-deps glib libpng libwebp libexif libxml2
libjpeg-turbo  
RUN git clone \--depth 1 --branch rpi https://github.com/Torlus/qemu.git  
RUN cd qemu && git checkout `cat /root/qemu.lock`  
RUN apk --update add qemu  
RUN wget "https://circle-artifacts.com/gh/andyshinn/alpine-pkg-
glibc/14/artifacts/0/home/ubuntu/alpine-pkg-
glibc/packages/builder/x86_64/glibc-2.22-r5.apk" \  
&& wget "https://circle-artifacts.com/gh/andyshinn/alpine-pkg-
glibc/14/artifacts/0/home/ubuntu/alpine-pkg-
glibc/packages/builder/x86_64/glibc-bin-2.22-r5.apk" \  
&& apk add --allow-untrusted glibc-2.22-r5.apk glibc-bin-2.22-r5.apk \  
&& /usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib  
RUN apk --update add linux-headers  
RUN apk --update add pixman-dev  
RUN cd qemu && git submodule update --init dtc  
COPY socket_scm_helper.c /qemu/tests/qemu-iotests/  
COPY signal.h /usr/include/sys/  
COPY qemu-openpty.c /qemu/util/  
COPY limits.h /usr/include/bits/  
COPY pci.c /qemu/hw/pci/  
RUN head -n 20 /qemu/tests/qemu-iotests/socket_scm_helper.c  
RUN head /usr/include/sys/signal.h  
RUN cd qemu && ./configure --prefix=/opt/qemu-rpi --target-list=arm-softmmu &&
make && make install  
RUN for i in `seq 0 7`; do mknod /dev/loop$i b -m0660 7 $i; done  
  
ADD emupi /root/emupi  
ADD rpimount /root/rpimount  
ADD blkoffset /root/blkoffset  
ADD qemu.lock /root/qemu.lock  
  
RUN apk del build-deps dev-deps run-deps \  
&& rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["/root/emupi", "/rpi.img"]  

