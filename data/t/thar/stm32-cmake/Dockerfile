FROM ubuntu:16.04  
RUN apt-get update && apt-get --yes --force-yes install git cmake
libusb-1.0-0-dev wget bzip2  
RUN mkdir toolchain && cd toolchain && wget -qO-
https://armkeil.blob.core.windows.net/developer/Files/downloads/gnu-
rm/6_1-2017q1/gcc-arm-none-eabi-6-2017-q1-update-linux.tar.bz2 | tar xj && cp
-r gcc-arm-none-eabi-6-2017-q1-update/* /usr/ && cd .. && rm -rf toolchain  
RUN apt-get clean  
RUN mkdir /app  
RUN cd /app && git clone https://github.com/texane/stlink.git && cd stlink &&
make release && cd build/Release/ && make install && cd /app && rm -rf stlink  
RUN ldconfig  
COPY stm32-cmake/cmake /usr/share/cmake-3.5/Modules/  
COPY STM32Cube_FW_F4_V1.14.0 /opt/STM32Cube_FW_F4_V1.14.0  
COPY STM32F4xx_DSP_StdPeriph_Lib_V1.8.0
/opt/STM32F4xx_DSP_StdPeriph_Lib_V1.8.0  
COPY compile.sh /usr/local/bin/  
WORKDIR /app/  
CMD compile.sh  

