ARG QEMU_VERSION=2.11.0  
ARG QEMU_ARCH=x86_64  
  
FROM centos:7 as builder  
ARG QEMU_VERSION  
ARG QEMU_ARCH  
  
RUN yum -y install cpio \  
rpm2cpio \  
wget  
  
RUN mkdir artifacts \  
&& cd artifacts \  
&& wget
https://kojipkgs.fedoraproject.org/packages/qemu/${QEMU_VERSION}/4.fc28.1/${QEMU_ARCH}/qemu-
user-static-${QEMU_VERSION}-4.fc28.1.${QEMU_ARCH}.rpm \  
&& ls -lh \  
&& rpm2cpio qemu-user-static-${QEMU_VERSION}-4.fc28.1.${QEMU_ARCH}.rpm | cpio
-dimv \  
&& ls -lhR  
  
FROM scratch  
COPY \--from=builder /artifacts/usr/bin /usr/bin/qemu  
VOLUME /usr/bin/qemu

