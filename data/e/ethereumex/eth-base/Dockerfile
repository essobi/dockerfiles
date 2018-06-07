FROM ethereum/client-cpp  
  
# alpine sdk - curl, gcc, make, g++, git  
RUN apk add --update \  
alpine-sdk \  
bash \  
vim \  
python \  
net-tools \  
nodejs \  
nodejs-npm \  
lsof  
  
RUN npm install -g pm2  
  
RUN addgroup -g 99 -S eth-node  
RUN adduser -u 99 -D -S -G eth-node eth-node  
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
  
ENTRYPOINT ["/bin/sh"]  

