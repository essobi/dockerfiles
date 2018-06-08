#########################################################################################  
#  
# Boot an OS securely over an insecure network.  
#  
#########################################################################################  
  
# Usage:  
# docker run --rm -t -i \  
# -v /path/to/certificates:/vapr/certstore:ro \  
# -v /path/to/tls_key:/vapr/keys/tls_key:ro \  
# -v "${VAPR_BUILDDIR:=`pwd`}":/vapr/build \  
# sojournlabs/ipxe_builder \  
# imageserver1 templateserver1 imageserver2 templateserver2 ...  
#  
# The tls_key must have a corresponding .crt file in /vapr/certstore  
# (differing only in extension -- key and crt, respectively).  
# This image will attempt to boot using a kernel from imageserver1 and
securely grab  
# configuration information (where applicable) from templateserver1 via the
boot server  
# in https://github.com/SojournLabs/netboot. The iPXE image will fall back to
servers  
# 2, 3, 4, etc. until one is found and then abort to an iPXE boot prompt.  
  
FROM sojournlabs/gcc  
MAINTAINER jonathan lung <vapr@sojournlabs.com>  
RUN apt-get update && apt-get install -y \  
genisoimage \  
liblzma-dev \  
syslinux  
RUN mkdir -p /vapr  
WORKDIR /vapr  
ENV PATH /vapr:$PATH  
# Download ipxe  
RUN git clone git://git.ipxe.org/ipxe.git  
WORKDIR /vapr/ipxe/src  
# Enable HTTPS and image signing.  
RUN sed -i 's/undef\tDOWNLOAD_PROTO_HTTPS/define\tDOWNLOAD_PROTO_HTTPS/'
config/general.h  
RUN sed -i 's|//#define IMAGE_TRUST_CMD|#define\tIMAGE_TRUST_CMD|'
config/general.h  
RUN sed -i 's|//#define IMAGE_TRUST_CMD|#define\tIMAGE_TRUST_CMD|'
config/general.h  
RUN sed -i 's|//#define PING_CMD|#define\tPING_CMD|' config/general.h  
# Do a preliminary build to save time later.  
RUN make  
ADD build_ipxe /bin/build_ipxe  
WORKDIR /vapr  
VOLUME ["/vapr/keys", "/vapr/certstore", "/vapr/build"]  
ENTRYPOINT ["/bin/build_ipxe"]

