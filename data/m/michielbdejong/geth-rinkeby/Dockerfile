FROM ubuntu  
RUN apt-get update  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository -y ppa:ethereum/ethereum  
RUN apt-get update  
RUN apt-get install -y ethereum wget git vim  
RUN wget https://www.rinkeby.io/rinkeby.json  
RUN geth --datadir=$HOME/.rinkeby init rinkeby.json  
RUN wget https://dl.dropboxusercontent.com/u/4270001/testnet_genesis.json  
RUN mv testnet_genesis.json ropsten.json  
RUN geth --datadir=$HOME/.ropsten init ropsten.json  
EXPOSE 8545  
EXPOSE 30303  
EXPOSE 30303/udp  
# To run a rinkeby archive node:  
#CMD geth --networkid=4 --datadir=$HOME/.rinkeby --cache=1024 --syncmode=full
--ethstats='yournode:Respect my authoritah!@stats.rinkeby.io'
--bootnodes=enode://a24ac7c5484ef4ed0c5eb2d36620ba4e4aa13b8c84684e1b4aab0cebea2ae45cb4d375b77eab56516d34bfbd3c1a833fc51296ff084b770b94fb9028c4d25ccf@52.169.42.101:30303?discport=30304
--rpc --rpcapi="personal,eth,network" --rpcaddr "127.0.0.1"  
# To run a rinkeby full node:  
CMD geth --networkid=4 --datadir=$HOME/.rinkeby --cache=128
--ethstats='yournode:Respect my authoritah!@stats.rinkeby.io'
\--bootnodes=enode://a24ac7c5484ef4ed0c5eb2d36620ba4e4aa13b8c84684e1b4aab0cebea2ae45cb4d375b77eab56516d34bfbd3c1a833fc51296ff084b770b94fb9028c4d25ccf@52.169.42.101:30303?discport=30304
--rpc --rpcapi="personal,eth,network" \--rpcaddr "127.0.0.1"  
  
# To run a ropsten full node:  
#CMD geth --networkid=3 --datadir=$HOME/.ropsten --cache=128 --bootnodes
"enode://20c9ad97c081d63397d7b685a412227a40e23c8bdc6688c6f37e97cfbc22d2b4d1db1510d8f61e6a8866ad7f0e17c02b14182d37ea7c3c8b9c2683aeb6b733a1@52.169.14.227:30303,enode://6ce05930c72abc632c58e2e4324f7c7ea478cec0ed4fa2528982cf34483094e9cbc9216e7aa349691242576d552a2a56aaeae426c5303ded677ce455ba1acd9d@13.84.180.240:30303"
--rpc --rpcapi="personal,eth,network" --rpcaddr "127.0.0.1"  
# To run a rinkeby light node:  
#CMD geth --networkid=4 --datadir=$HOME/.rinkeby --syncmode=light
--ethstats='yournode:Respect my authoritah!@stats.rinkeby.io'
--bootnodes=enode://a24ac7c5484ef4ed0c5eb2d36620ba4e4aa13b8c84684e1b4aab0cebea2ae45cb4d375b77eab56516d34bfbd3c1a833fc51296ff084b770b94fb9028c4d25ccf@52.169.42.101:30303?discport=30304
--rpc --rpcapi="personal,eth,network" --rpcaddr "127.0.0.1"  
# To run a rinkeby embedded node (experimental):  
# CMD geth --networkid=4 --datadir=$HOME/.rinkeby --cache=32 --syncmode=light
--ethstats='yournode:Respect my authoritah!@stats.rinkeby.io'
--bootnodes=enode://a24ac7c5484ef4ed0c5eb2d36620ba4e4aa13b8c84684e1b4aab0cebea2ae45cb4d375b77eab56516d34bfbd3c1a833fc51296ff084b770b94fb9028c4d25ccf@52.169.42.101:30303?discport=30304
--rpc --rpcapi="personal,eth,network" --rpcaddr "127.0.0.1"  

