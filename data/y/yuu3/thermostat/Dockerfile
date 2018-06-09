FROM golang:1.9.2  
RUN apt update && apt install -y gccgo-6-arm-linux-gnueabihf  
  
ENV PKG_CONFIG_PATH "/usr/lib/arm-linux-gnueabihf/pkgconfig"  
ADD libusb-1.0-0-dev_1.0.19-1_armhf.tar.bz2 /  
ADD libudev1_215-17+deb8u7_armhf.tar.bz2 /

