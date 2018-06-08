FROM ubuntu:16.04  
MAINTAINER "Romain Acciari" <romain.acciari@openio.io>  
  
RUN apt-get update \  
&& apt -y install debootstrap qemu-user-static qemu-system-aarch64 qemu-user-
static linux-libc-dev-arm64-cross libc6-arm64-cross  
  
VOLUME ["/mnt"]  
  
ADD debootstrap.sh /  
ADD scripts /scripts/  
  
CMD ["/debootstrap.sh"]  
#docker run --privileged -v /mnt/:/mnt/ --net=host ubuntu:16.04 /bin/bash  

