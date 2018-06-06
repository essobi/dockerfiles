FROM ubuntu  
MAINTAINER Dinesh Auti dauti@uncc.edu  
  
ENV HOME /root  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends build-essential gdb gcc-multilib
git ca-certificates libsdl1.2-dev libtool-bin libglib2.0-dev libz-dev
libpixman-1-dev && \  
rm -rf /var/lib/apt/lists/* && \  
cd $HOME && \  
git clone http://web.mit.edu/ccutler/www/qemu.git -b 6.828-2.3.0 && \  
cd qemu && \  
./configure --disable-kvm --target-list="i386-softmmu x86_64-softmmu" && \  
make && make install && cd .. && \  
rm -r qemu  
  

