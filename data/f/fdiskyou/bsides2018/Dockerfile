# Dockerfile for The Linux Heap Exploitation Workshop @ BSides 2018  
FROM ubuntu:14.04  
MAINTAINER rui@deniable.org  
  
ENV MALLOC_CHECK_ 0  
ENV WRKSRC /opt  
ENV WRKDIR /root/labs  
  
RUN apt-get update && apt-get upgrade -y && apt-get install -y sudo git build-
essential gdb wget && \  
apt-get -y install curl vim gcc gcc-multilib g++-multilib eglibc-source && \  
mkdir -p $WRKDIR && cd /usr/src/glibc && tar xf eglibc-2.19.tar.xz && \  
mkdir -p $WRKSRC && cd $WRKSRC && \  
git clone https://github.com/pwndbg/pwndbg && \  
cd pwndbg && ./setup.sh && \  
cd $WRKSRC && \  
git clone https://github.com/Svenito/exploit-pattern && \  
git clone https://github.com/n30m1nd/Linux_Heap_Exploitation_Intro_Series && \  
echo "dir /usr/src/glibc/eglibc-2.19/malloc/" >> /root/.gdbinit && \  
apt-get -qy clean autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR $WRKDIR  
ENTRYPOINT ["/bin/bash"]  

