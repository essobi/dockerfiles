FROM debian:8  
  
MAINTAINER xdxd <http://xdxd.love>  
  
RUN apt-get update && apt-get install -y qemu-user-static \  
&& apt-get install -y net-tools && apt-get install -y tcpdump \  
&& apt-get install -y file && apt-get install -y elfutils  
# COPY docker-entrypoint.sh /entrypoint.sh  
# CMD [cd /root/dlink605 && chroot . ./qemu -g 1234 -E LD_PRELOAD="/apmib-
ld.so" bin/boa -d]

