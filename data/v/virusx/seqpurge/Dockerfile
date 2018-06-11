FROM ubuntu:16.04  
ENV SEQPURGE_VERSION="32d9c85395a"  
RUN apt-get update && \  
apt-get install -y git build-essential g++ qt5-default libqt5xmlpatterns5-dev
libqt5sql5-mysql git cmake python python-matplotlib && \  
cd /root/ && git clone --recursive https://github.com/imgag/ngs-bits && cd
ngs-bits && git checkout ${SEQPURGE_VERSION} && \  
sed -i "s/[^qc]make;/ make -j$(nproc);/g" Makefile && sed -i "s/[^qc]make$/
make -j$(nproc)/g" Makefile && \  
make build_3rdparty && make build_tools_release && \  
cp bin/SeqPurge /usr/bin/ && cp bin/libcppCORE.so.1 bin/libcppNGS.so.1
bin/libcppXML.so.1 bin/libbamtools.so.2.4.1 /usr/lib/ && \  
rm -rf /root/ngs-bits && \  
apt-get purge -y build-essential git g++ qt5-default libqt5xmlpatterns5-dev
libqt5sql5-mysql cmake python-matplotlib && \  
apt-get autoremove -y \--purge && apt-get install -y libqt5core5a libqt5xml5
libqt5xmlpatterns5 &&\  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

