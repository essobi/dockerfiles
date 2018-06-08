FROM debian:stretch-slim as qemu_builder  
  
ENV QEMU_VERSION v2.11.1  
RUN apt-get update -q && apt-get install -q -y \  
git \  
build-essential flex bison \  
pkg-config \  
python \  
zlib1g-dev libpixman-1-dev libglib2.0-dev libfdt-dev  
  
RUN git clone git://git.qemu-project.org/qemu.git && \  
cd qemu && \  
git checkout tags/$QEMU_VERSION && \  
git submodule update --init dtc  
  
WORKDIR /qemu  
RUN ./configure --target-list=x86_64-softmmu \  
\--disable-tpm \  
\--disable-libiscsi \  
\--disable-libnfs \  
\--disable-fdt \  
\--disable-glusterfs \  
\--disable-linux-user \  
\--disable-bsd-user \  
\--disable-guest-agent \  
\--static  
  
RUN make  
RUN make DESTDIR=/tarball install  
  
FROM alpine:3.7  
COPY \--from=qemu_builder /tarball /  
CMD ["qemu-system-x86_64"]

