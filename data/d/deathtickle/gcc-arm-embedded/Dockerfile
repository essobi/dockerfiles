FROM ubuntu:latest  
  
RUN apt-get update && apt-get -y install software-properties-common wget  
  
RUN add-apt-repository ppa:team-gcc-arm-embedded/ppa  
  
RUN apt-get update && apt-get -y install gcc-arm-embedded make cppcheck  
  
RUN wget -O - https://github.com/gnu-mcu-
eclipse/qemu/releases/download/gae-2.8.0-20170301/gnuarmeclipse-qemu-
debian64-2.8.0-201703022210-head.tgz \  
| tar -xz && \  
ln -s gnuarmeclipse/qemu/2.8.0-201703022210-head/qemu-system-gnuarmeclipse
bin/qemu-system-gnuarmeclipse  

