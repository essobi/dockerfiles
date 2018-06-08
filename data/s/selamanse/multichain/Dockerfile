FROM ubuntu:16.04  
  
MAINTAINER selamanse <selamanse@scheinfrei.info>  
  
ENV CHAINNAME chain1  
ENV MULTICHAIN_VERSION 1.0.2  
  
RUN apt-get update && \  
apt-get install -y wget tar  
  
RUN wget
https://www.multichain.com/download/multichain-${MULTICHAIN_VERSION}.tar.gz &&
\  
tar -xvzf multichain-${MULTICHAIN_VERSION}.tar.gz && \  
rm -f multichain-${MULTICHAIN_VERSION}.tar.gz && \  
cd multichain-${MULTICHAIN_VERSION} && \  
mv multichaind multichain-cli multichain-util /usr/local/bin  
  
# some default overrides from params.dat that come handy to start without
hassle  
ENV MC_ANYONE_CAN_CONNECT true  
ENV MC_ANYONE_CAN_SEND true  
ENV MC_ANYONE_CAN_RECEIVE true  
ENV MC_ANYONE_CAN_RECEIVE_EMPTY true  
ENV MC_ANYONE_CAN_CREATE true  
ENV MC_ANYONE_CAN_ISSUE true  
ENV MC_ANYONE_CAN_MINE true  
ENV MC_ANYONE_CAN_ACTIVATE true  
ENV MC_ANYONE_CAN_ADMIN true  
ENV MC_MAX_STD_TX_SIZE 100000  
ENV MC_MAX_STD_OP_RETURNS_COUNT 10  
ENV MC_MAX_STD_OP_RETURN_SIZE 4096  
ENV MC_MAX_STD_OP_DROPS_COUNT 5  
ENV MC_MAX_STD_ELEMENT_SIZE 600  
ENV NETWORK_PORT 8571  
ENV RPC_PORT 8570  
ENV RPC_ALLOW_IP 0.0.0.0/0.0.0.0  
ENV RPC_USER multichainrpc  
ENV RPC_PASSWORD multichain  
  
CMD if [ ! -f /root/.multichain/${CHAINNAME}/params.dat ]; then multichain-
util create ${CHAINNAME} \  
-anyone-can-connect=${MC_ANYONE_CAN_CONNECT} \  
-anyone-can-send=${MC_ANYONE_CAN_SEND} \  
-anyone-can-receive=${MC_ANYONE_CAN_RECEIVE} \  
-anyone-can-receive-empty=${MC_ANYONE_CAN_RECEIVE_EMPTY} \  
-anyone-can-create=${MC_ANYONE_CAN_CREATE} \  
-anyone-can-issue=${MC_ANYONE_CAN_ISSUE} \  
-anyone-can-mine=${MC_ANYONE_CAN_MINE} \  
-anyone-can-activate=${MC_ANYONE_CAN_ACTIVATE} \  
-anyone-can-admin=${MC_ANYONE_CAN_ADMIN} \  
-max-std-tx-size=${MC_MAX_STD_TX_SIZE} \  
-max-std-op-returns-count=${MC_MAX_STD_OP_RETURNS_COUNT} \  
-max-std-op-return-size=${MC_MAX_STD_OP_RETURN_SIZE} \  
-max-std-op-drops-count=${MC_MAX_STD_OP_DROPS_COUNT} \  
-max-std-element-size=${MC_MAX_STD_ELEMENT_SIZE} \  
-default-network-port=${NETWORK_PORT} \  
-default-rpc-port=${RPC_PORT} \  
-max-std-element-size=${MC_MAX_STD_ELEMENT_SIZE}; fi && \  
multichaind \  
-server \  
-rest \  
-printtoconsole \  
-rpcuser=${RPC_USER} \  
-rpcpassword=${RPC_PASSWORD} \  
-port=${NETWORK_PORT} \  
-rpcport=${RPC_PORT} \  
-rpcallowip=${RPC_ALLOW_IP} \  
${CHAINNAME}  

