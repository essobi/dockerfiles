FROM nvidia/cuda:9.1-devel  
ENTRYPOINT ["/home/miner/entrypoint.sh"]  
  
RUN groupadd -g 2000 miner && \  
useradd -u 2000 -g miner -m -s /bin/bash miner && \  
echo 'miner:miner' | chpasswd  
RUN apt-get -y update  
RUN apt-get -y install git automake libssl-dev libcurl4-openssl-dev  
  
COPY entrypoint.sh /home/miner/  
RUN chmod +x /home/miner/entrypoint.sh  
RUN chown miner:miner /home/miner/entrypoint.sh  
  
USER miner  
RUN cd && git clone https://github.com/tpruvot/ccminer.git  
RUN cd ~/ccminer && ./autogen.sh && ./configure --with-cuda=/usr/local/cuda &&
make -j$(($(nproc)+1))  

