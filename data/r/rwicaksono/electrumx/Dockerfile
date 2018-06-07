FROM python:3.6  
# Prepare user  
RUN useradd -ms /bin/bash zcluser  
WORKDIR /home/zcluser  
  
# Install zcl dependencies  
RUN apt-get update  
RUN apt-get install -y apt-utils  
RUN apt-get install -y libleveldb1 libleveldb-dev  
RUN apt-get install -y build-essential pkg-config libc6-dev m4 g++-multilib
autoconf libtool ncurses-dev unzip git python zlib1g-dev wget bsdmainutils
automake  
  
# Build zcl node daemon  
RUN git clone https://github.com/z-classic/zclassic  
RUN mkdir /home/zcluser/zcl_electrum_db  
RUN /home/zcluser/zclassic/zcutil/build.sh -j$(nproc)  
  
# Install electrumx dependencies  
RUN pip install pylru==1.0.9  
RUN pip install aiohttp==1.0.5  
RUN pip install x11_hash==1.4  
RUN pip install plyvel==0.9  
  
COPY run_electrumx_docker.sh /home/zcluser/run_electrumx_docker.sh  
RUN chown -R zcluser:zcluser /home/zcluser/zcl_electrum_db
/home/zcluser/run_electrumx_docker.sh  
RUN chmod 755 /home/zcluser/run_electrumx_docker.sh  
  
USER zcluser  
RUN /home/zcluser/zclassic/zcutil/fetch-params.sh  
RUN git clone https://github.com/BTCP-community/electrumx.git  
RUN wget -q
https://github.com/z-classic/zclassic/releases/download/Config/zclassic.conf  
RUN sed -ie '/^rpcport=8232/a txindex=1' zclassic.conf  
  
ENTRYPOINT ["/bin/sh", "-c", "/home/zcluser/run_electrumx_docker.sh"]  

