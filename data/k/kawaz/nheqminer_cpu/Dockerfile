FROM ubuntu:16.04 AS BUILD  
RUN apt-get update && apt-get install -y git cmake build-essential libboost-
all-dev && apt-get clean && rm -rf /var/lib/apt/lists/*  
WORKDIR /build  
RUN git clone \--depth 1 https://github.com/nicehash/nheqminer.git && \  
cd nheqminer/cpu_xenoncat/asm_linux/ && chmod +x fasm && sh assemble.sh && cd
../../.. && \  
mkdir build && cd build && \  
cmake -DUSE_CUDA_DJEZO=OFF ../nheqminer && \  
make -j $(nproc) && \  
cp nheqminer /usr/bin/nheqminer_cpu && ln -s nheqminer_cpu /usr/bin/nheqminer
&& \  
ldd /usr/bin/nheqminer_cpu | grep -Eo '/[^ ]+' > /build/nheqminer_cpu.dep_ldd
&& \  
dpkg -S $(cat /build/nheqminer_cpu.dep_ldd) | perl -pe's/:.*//' | sort -u >
/build/nheqminer_cpu.dep_packages  
  
FROM ubuntu:16.04  
COPY \--from=BUILD /usr/bin/nheqminer_cpu /usr/bin/nheqminer /usr/bin/  
COPY \--from=BUILD /build/nheqminer_cpu.dep_packages /  
RUN apt-get update && apt-get install -y inetutils-ping $(cat
/nheqminer_cpu.dep_packages) --no-install-recommends && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /nheqminer_cpu.dep_packages  
ENV \  
SERVER= \  
WALLET=361yTPdoXcBpWRJDpPJSoC2v5Ss3fYM3FL \  
WORKER=  
ADD bootstrap.sh bootstrap.sh  
ENTRYPOINT [ "./bootstrap.sh" ]  

