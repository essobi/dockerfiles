# BUILD-USING:  docker build -t drewbug/nook2_1-2_base .  
  
FROM ubuntu:12.04  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -y  
MAINTAINER Drew Carey Buglione <me@drewb.ug>  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget ca-certificates
bzip2  
  
RUN wget https://sourcery.mentor.com/GNUToolchain/package6488/public/arm-none-
linux-gnueabi/arm-2010q1-202-arm-none-linux-gnueabi-i686-pc-linux-gnu.tar.bz2
&& \  
tar xvfj arm-2010q1-202-arm-none-linux-gnueabi-i686-pc-linux-gnu.tar.bz2 && \  
rm arm-2010q1-202-arm-none-linux-gnueabi-i686-pc-linux-gnu.tar.bz2  
ENV PATH /arm-2010q1/bin:$PATH  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential lib32z1
lib32ncurses5 lib32bz2-1.0 lib32asound2  
  
ENV ARCH arm  
ENV CROSS_COMPILE arm-none-linux-gnueabi-  
  
RUN wget http://images.barnesandnoble.com/PResources/download/Nook/source-
code/nook2_1-2.tgz && \  
tar xvfz nook2_1-2.tgz && \  
rm nook2_1-2.tgz  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y uboot-mkimage  

