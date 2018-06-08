FROM fdiskyou/afl-qemu:0.1  
MAINTAINER rui@deniable.org  
  
# check https://hub.docker.com/u/fdiskyou/ for more information  
ENV K kern  
ENV WRKSRC /opt  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get -y upgrade && \  
apt-get -yq install linux-image-$(uname -r) && cd $WRKSRC && \  
git clone https://github.com/nccgroup/TriforceAFL.git && \  
cd TriforceAFL && make && cd .. && \  
git clone https://github.com/nccgroup/TriforceLinuxSyscallFuzzer.git && \  
cd TriforceLinuxSyscallFuzzer && make && mkdir -p $K && \  
cp /boot/vmlinuz* kern/bzImage && \  
cp /boot/System.map* kern/kallsyms && \  
make inputs && \  
apt-get -qy clean autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
CMD ["/bin/bash"]  

