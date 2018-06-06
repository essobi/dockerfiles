# Pull base image  
FROM resin/rpi-raspbian:jessie  
MAINTAINER philipz <philipzheng@gmail.com>  
  
ENV QEMU_EXECVE 1  
COPY qemu/cross-build-end qemu/cross-build-start qemu/qemu-arm-static qemu/sh-
shim /usr/bin/  
RUN [ "cross-build-start" ]  
  
RUN apt-get update && apt-get install -y bash git subversion make sudo fpc
fpc-source binutils build-essential zip unzip wget libusb-dev libsane-dev
sqlite3 postgresql-client binutils libgtk2.0-0 libgtk2.0-dev psmisc && rm -rf
/var/lib/apt/lists/*  
  
RUN svn co http://svn.freepascal.org/svn/lazarus/branches/fixes_1_6 lazarus  
RUN cd lazarus && \  
make bigide && \  
make install  
  
COPY environmentoptions.xml /root/.lazarus/  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["bash"]  
  
RUN [ "cross-build-end" ]  

