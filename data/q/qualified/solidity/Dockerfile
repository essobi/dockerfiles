FROM node:8.9.4-stretch  
# Truffle 4.0.6 (solc 0.4.19)  
# No TestRPC is needed  
RUN set -ex; \  
useradd --create-home codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
ENV NPM_CONFIG_LOGLEVEL=warn NODE_ENV=production  
  
COPY rootfs/workspace/solidity /workspace/solidity  
RUN chown -R codewarrior:codewarrior /workspace/solidity  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior \  
PATH=/workspace/solidity/node_modules/.bin:$PATH  
  
RUN cd /workspace/solidity && yarn install \--production=false  

