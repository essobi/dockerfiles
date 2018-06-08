FROM ethcore/parity:beta-release  
  
RUN ln -s /build/parity/target/release/parity /usr/bin/parity  
  
RUN apt-get update  
RUN apt-get install -y curl  
RUN curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -  
RUN apt-get update  
RUN apt-get install -y apt-utils  
RUN apt-get install -y vim  
RUN apt-get install -y net-tools  
RUN apt-get -y install nodejs  
# RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN apt-get -y install git  
RUN apt-get -y install lsof  
RUN npm install -g npm pm2  
  
RUN useradd -ms /bin/bash eth-node  
RUN mkdir -p /home/geth/.geth  
RUN chown -R eth-node /home/geth  
  
USER eth-node  
WORKDIR /home/eth-node  
  
RUN pm2 install pm2-logrotate  
RUN pm2 set pm2-logrotate:max_size 100M  
RUN pm2 set pm2-logrotate:compress true  
RUN pm2 set pm2-logrotate:rotateInterval '23 * * *'  
  
RUN git clone https://github.com/EthereumEx/bootnode-registrar.git /home/eth-
node/lib/bootnode  
WORKDIR /home/eth-node/lib/bootnode  
RUN npm install  
  
RUN git clone https://github.com/EthereumEx/eth-net-intelligence-api.git
/home/eth-node/lib/ethStatsApi  
WORKDIR /home/eth-node/lib/ethStatsApi  
RUN npm install  
  
ENTRYPOINT ["/bin/bash"]  

