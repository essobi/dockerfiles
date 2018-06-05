FROM gcc:4.9.4  
MAINTAINER Mike Cutalo <mcutalo88@gmail.com>  
  
ARG release=1.1  
RUN git clone https://github.com/uraymeiviar/burst-miner.git /burst-miner  
WORKDIR /burst-miner  
RUN git checkout tags/$release  
RUN make  
  
ENTRYPOINT /burst-miner/bin/burstminer /burst-miner/mining.conf  

