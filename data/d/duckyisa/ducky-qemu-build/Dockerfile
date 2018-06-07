FROM docker.io/fedora  
  
MAINTAINER Milos Prchlik <happz@happz.cz>  
  
ARG BUILD_DATE  
ARG IMAGE_VERSION  
ARG IMAGE_RELEASE  
ARG QEMU_VERSION  
ARG VCS_REF  
  
LABEL version=$IMAGE_VERSION \  
release=$IMAGE_RELEASE \  
org.label-schema.schema-version="1.0" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="happz/ducky-qemu" \  
org.label-schema.description="QEMU (https://www.qemu.org/) is a generic and
open source machine & userspace emulator and virtualizer. This is a QEMU build
with support for running binaries compiled for Ducky platform
(https://duckyisa.github.io/)." \  
org.label-schema.usage="/usr/doc/ducky-qemu-docker-usage.txt" \  
org.label-schema.url="https://duckyisa.github.io/docs/qemu.html" \  
org.label-schema.vcs-url="https://github.com/DuckyISA/ducky-qemu-build" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vendor="DuckyISA" \  
org.label-schema.version=$QEMU_VERSION \  
org.label-schema.docker.cmd="docker run --rm -it -v /app/directory:/APP ducky-
qemu [QEMU options] -device loader,file=/APP/app-binary,addr=0x20000
-nographic" \  
org.label-schema.docker.cmd.help="docker run --rm ducky-qemu --help"  
  
RUN dnf update -y \  
&& dnf install -y dnf-plugins-core \  
&& dnf copr -y enable happz/ducky-qemu \  
&& dnf install -y ducky-qemu \  
&& dnf clean all  
  
ENV PATH=/opt/ducky/bin:$PATH  
  
ENTRYPOINT ["/opt/ducky/bin/qemu-system-ducky"]  

