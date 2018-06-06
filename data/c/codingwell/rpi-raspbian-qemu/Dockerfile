FROM resin/rpi-raspbian  
  
ENV QEMU_EXECVE 1  
COPY . /usr/bin  
  
RUN [ "qemu-arm-static", "/bin/sh", "-c", "ln -s resin-xbuild /usr/bin/cross-
build-start; ln -s resin-xbuild /usr/bin/cross-build-end; mv /bin/sh
/bin/sh.real; ln -s /bin/sh.real /bin/sh" ]  

