FROM debian:jessie  
  
COPY *.sh /build/  
ENV COMMIT 19bd6df742e2a437b46eb69eb85e597135ecce8b  
  
RUN groupadd -g 1000 docker && useradd docker -u 1000 -g 1000 -s /bin/bash
--no-create-home  
  
ENV RUN_PACKAGES="make python python-serial"  
ENV BUILD_PACKAGES="unrar autoconf automake libtool gcc g++ gperf flex bison
texinfo gawk libncurses5-dev libexpat1-dev git ca-certificates wget bzip2
patch libtool-bin unzip"  
  
RUN /build/prepare.sh && chown -R docker:docker /build && su docker -c
"/build/build.sh" && mkdir -p /opt/esp-open-sdk/ && mv /build/esp-open-
sdk/xtensa-lx106-elf/ /opt/esp-open-sdk/ && /build/cleanup.sh  
  
RUN ln -s /opt/esp-open-sdk/xtensa-lx106-elf/xtensa-lx106-elf/sysroot/usr/lib/
/opt/esp-open-sdk/xtensa-lx106-elf/xtensa-lx106-elf/sysroot/usr/ld && mkdir -p
/opt/Espressif/crosstool-NG/builds/xtensa-lx106-elf/ && ln -s /opt/esp-open-
sdk/xtensa-lx106-elf/bin /opt/Espressif/crosstool-NG/builds/xtensa-
lx106-elf/bin && ln -s /opt/esp-open-sdk/xtensa-lx106-elf/xtensa-
lx106-elf/sysroot/usr /opt/Espressif/ESP8266_SDK  
  
USER docker  
ENV PATH /opt/esp-open-sdk/xtensa-lx106-elf/bin:$PATH  

