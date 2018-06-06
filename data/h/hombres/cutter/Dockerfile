FROM ubuntu:16.04  
MAINTAINER xirax (bad-hombres)  
  
WORKDIR /tmp  
RUN apt-get update -y  
RUN apt-get -y install wget \  
libsm6 \  
libfontconfig \  
libglib2.0-0 \  
libgl1-mesa-glx \  
libfuse2 \  
libnss3  
  
RUN wget
https://github.com/radareorg/cutter/releases/download/v1.4/Cutter-v1.4-x86_64.AppImage  
RUN chmod +x Cutter-v1.4-x86_64.AppImage  
  
CMD ["./Cutter-v1.4-x86_64.AppImage"]  

