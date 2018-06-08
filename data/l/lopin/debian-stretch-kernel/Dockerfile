FROM lopin/kernel-deb-builder as builder  
  
RUN mkdir -p /SRC/linux /build/linux && cd /SRC/linux && \  
apt-get update && apt-get --download-only source linux && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
ENV \  
DEBEMAIL='Martin Lopatář <lop.spm@seznam.cz>' \  
DEBCHANGE_OPTIONS='-l +smb3enc' \  
ARCH=amd64 \  
FEATURESET=none \  
FLAVOUR=amd64 \  
DEBIAN_KERNEL_DISABLE_DEBUG=yes  
  
COPY patches /SRC/patches  
COPY scripts /SRC  
  
VOLUME /build/linux  
  
RUN /SRC/build.sh  
  
FROM alpine:latest  
RUN mkdir /SRC /OUT  
COPY \--from=builder /SRC/* /SRC/  
COPY \--from=builder /build/* /OUT/  
  

