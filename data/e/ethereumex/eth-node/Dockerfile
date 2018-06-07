FROM ethereumex/eth-base:latest  
  
WORKDIR /home/eth-node/lib/bootnode  
RUN git pull  
RUN git reset --hard master  
RUN npm install  
  
WORKDIR /home/eth-node/lib/ethStatsApi  
RUN git pull  
RUN git reset --hard master  
RUN npm install  
  
WORKDIR /home/eth-node  
ADD app.json /home/eth-node/app.json  
ADD runEth.sh /home/eth-node/runNode.sh  
  
ENTRYPOINT ["pm2", "start", "--no-daemon", "app.json"]  

