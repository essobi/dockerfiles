FROM keydonix/parity-instantseal-node8:safe  
# TODO: stop using :safe once we get real deploy of fixed instantseal  
# TODO: use digest  
# TODO: vendor  
RUN apt-get update && apt-get -y install software-properties-common git make
&& \  
add-apt-repository ppa:ethereum/ethereum && \  
apt-get update && \  
apt-get install -y solc  
  
COPY . /maker-docker-poa  
  
WORKDIR /maker-docker-poa  
  
RUN /maker-docker-poa/scripts/run-parity-and-deploy.sh  
  
WORKDIR /  

