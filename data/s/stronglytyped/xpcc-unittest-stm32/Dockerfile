FROM stronglytyped/xpcc-build  
MAINTAINER Sascha Schade (strongly-typed) <stronglytyp3d@gmail.com>  
LABEL Description="Image for compiling and running unittest of xpcc for ARM
from git"  
WORKDIR /work  
  
ADD gdb.cmd /work/  
  
ENV SCONGFLAGS "-j4"  
# Checkout and Compile  
CMD git clone \--depth=1 https://github.com/roboterclubaachen/xpcc && \  
cd xpcc && \  
sed -i "s|stm32f4_discovery|${BOARD}|g" /work/xpcc/src/unittest_stm32.cfg && \  
sed -i "s|OPENOCD_IP|${OPENOCD_IP}|g" /work/gdb.cmd && \  
scons unittest target=stm32 && \  
arm-none-eabi-gdb build/unittest_stm32/executable.elf --command=../gdb.cmd
--batch  

