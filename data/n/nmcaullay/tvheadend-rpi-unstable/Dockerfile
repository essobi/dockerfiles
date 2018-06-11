FROM resin/rpi-raspbian  
  
ENV QEMU_EXECVE 1  
COPY cross-build-end cross-build-start qemu-arm-static sh-shim /usr/bin/  
  
RUN [ "cross-build-start" ]  
  
RUN apt-get update -y && apt-get install  
  
RUN [ "cross-build-end" ]  

