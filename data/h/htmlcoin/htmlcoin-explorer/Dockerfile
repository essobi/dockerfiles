FROM htmlcoin/htmlcoin-deps  
  
RUN npm install -g htmlcoincore-node  
RUN mkdir /home/node/mynode-data  
  
RUN htmlcoincore-node create -d /home/node/mynode-data /home/node/mynode  
  
WORKDIR /home/node/mynode  
RUN htmlcoincore-node install htmlcoin-api  
RUN htmlcoincore-node install htmlcoin-explorer  
  
COPY htmlcoincore-node.json /home/node/mynode/htmlcoincore-node.json  
COPY htmlcoin.conf /home/node/mynode/htmlcoin.conf  
  
USER root  
ENV version="2.0.3"  
RUN wget https://downloads.bushstar.co.uk/htmlcoin-${version}-linux64.tar.gz \  
&& tar -xvzf htmlcoin-${version}-linux64.tar.gz \  
&& cp htmlcoind /bin/htmlcoind  
USER node  
  
ENTRYPOINT ["htmlcoincore-node", "start", "-c", "/home/node/mynode"]

