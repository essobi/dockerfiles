# kentwait/bwa  
FROM kentwait/alpine-base  
MAINTAINER Kent Kawashima <kentkawashima@gmail.com>  
  
ENV BWA_VERSION 0.7.15  
ADD "https://downloads.sourceforge.net/project/bio-
bwa/bwa-${BWA_VERSION}.tar.bz2" /tmp/  
  
WORKDIR /tmp  
RUN apk update && apk upgrade \  
&& apk add --no-cache --virtual temp-pkgs \  
musl-dev \  
zlib-dev \  
make \  
gcc \  
&& tar xjf bwa-${BWA_VERSION}.tar.bz2 \  
&& rm bwa-${BWA_VERSION}.tar.bz2 \  
&& cd bwa-${BWA_VERSION} \  
# Make changes to compile in Alpine Linux  
# https://github.com/lh3/bwa/issues/73  
&& sed -i '1s/^/\\#include \<stdint.h\> \n/' kthread.c \  
&& sed -i 's/u_int32_t/uint32_t/g' *.c \  
&& sed -i 's/u_int32_t/uint32_t/g' *.h \  
&& make \  
&& chmod +x bwa \  
&& mv /tmp/bwa-${BWA_VERSION}/bwa /usr/bin/bwa \  
# Create data placeholders  
&& mkdir -p /data \  
# Remove temp  
&& apk del temp-pkgs \  
&& rm -rf /tmp/* /var/cache/apk/* /root/.wget-hsts /root/.[acpw]*  
  
WORKDIR /data  
VOLUME /data  
ENTRYPOINT ["/init", "bwa"]  

