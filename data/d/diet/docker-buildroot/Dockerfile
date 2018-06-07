FROM ubuntu:latest  
  
RUN apt-get update && apt-get install -y bc wget curl git libncurses5-dev
build-essential unzip  
  
ADD http://buildroot.uclibc.org/downloads/buildroot-2014.08.tar.bz2
/tmp/buildroot.tar.bz2  
RUN tar jxf /tmp/buildroot.tar.bz2 && mv /buildroot-2014.08 /buildroot && rm
/tmp/buildroot.tar.bz2  
  
ADD bin/silent.sh /app/bin/silent  
ADD bin/build.sh /app/bin/build  
ADD bin/menu.sh /app/bin/menu  
ADD bin/miniconfig.sh /app/bin/miniconfig  
ADD bin/env /app/bin/env  
  
ADD rootfs /app/rootfs  
  
ENV BR2_EXTERNAL "/data"  
ENV PATH /app/bin:$PATH  
ENV KCONFIG_ALLCONFIG /data/mini.config  
  
VOLUME ["/data"]  
  
WORKDIR /buildroot  
  
CMD ["/app/bin/silent"]  

