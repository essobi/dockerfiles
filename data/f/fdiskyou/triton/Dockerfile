FROM ubuntu:16.04  
MAINTAINER rui@deniable.org  
  
LABEL description="Base image for Triton"  
  
ENV WRKSRC /opt  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get dist-upgrade -y && \  
apt-get install -y git cmake build-essential clang ca-certificates curl && \  
apt-get install -y unzip libboost-dev python-dev python-pip && \  
cd $WRKSRC && \  
curl -o z3.tgz -L https://github.com/Z3Prover/z3/archive/z3-4.5.0.tar.gz && \  
tar zxf z3.tgz && cd z3-z3-4.5.0 && \  
CC=clang CXX=clang++ python scripts/mk_make.py && cd build && make \  
&& make install && \  
cd $WRKSRC && \  
curl -o cap.tgz -L https://github.com/aquynh/capstone/archive/3.0.4.tar.gz &&
\  
tar xvf cap.tgz && cd capstone-3.0.4/ && ./make.sh install && \  
cd $WRKSRC && \  
curl -o pin.tgz -L
http://software.intel.com/sites/landingpage/pintool/downloads/pin-2.14-71313-gcc.4.4.7-linux.tar.gz
&& tar zxf pin.tgz && \  
cd /opt/pin-2.14-71313-gcc.4.4.7-linux/source/tools/ && \  
curl -o master.zip -L
https://github.com/JonathanSalwan/Triton/archive/master.zip && unzip
master.zip && cd Triton-master/ && mkdir build && cd build && \  
cmake -G "Unix Makefiles" -DPINTOOL=on -DKERNEL4=on .. && make install && \  
useradd -s /bin/bash -m triton && \  
echo triton:triton | chpasswd && usermod -aG sudo triton && \  
rm -rf /var/lib/apt/lists/*  
  
USER triton  
WORKDIR /home/triton  
ENV HOME /home/triton  
CMD ["/bin/bash"]  

