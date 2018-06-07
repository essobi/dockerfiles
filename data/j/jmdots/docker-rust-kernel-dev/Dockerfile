FROM debian:stable  
RUN apt-get update \  
&& apt-get install -y \  
binutils \  
bsdmainutils \  
gcc \  
grub \  
grub-pc-bin \  
grub-pc-dbg \  
nasm \  
xorriso \  
qemu \  
&& apt-get clean  
VOLUME ["/wrk"]  
CMD ["bash"]  

