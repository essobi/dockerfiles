FROM archlinux/base  
  
RUN set -e; \  
set -x; \  
pacman -Sy --noconfirm arm-none-eabi-binutils \  
arm-none-eabi-gcc \  
arm-none-eabi-newlib \  
doxygen \  
graphviz \  
make \  
python; \  
pacman -Scc --noconfirm  

