FROM resin/armv7hf-debian  
  
ENV QEMU_EXECVE 1  
COPY qemu-arm-static /usr/bin  
COPY resin-xbuild /usr/bin  
  
RUN [ "qemu-arm-static", "/bin/sh", "-c", "ln -s resin-xbuild /usr/bin/cross-
build-start; ln -s resin-xbuild /usr/bin/cross-build-end; ln /bin/sh
/bin/sh.real" ]  
  
# Set the env variable DEBIAN_FRONTEND to noninteractive to get  
# apt-get working without error output.  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN [ "cross-build-start" ]  
RUN apt-get update && \  
apt-get -y dist-upgrade && \  
apt-get -y autoremove  
RUN [ "cross-build-end" ]  
  
ENTRYPOINT [ "/bin/bash" ]

