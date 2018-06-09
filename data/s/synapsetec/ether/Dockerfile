FROM synapsetec/nodejs:node7  
RUN apt-get update && \  
apt-get install software-properties-common -y \--no-install-recommends && \  
add-apt-repository -y ppa:ethereum/ethereum && \  
apt-get update && \  
apt-get install ethereum -y \--no-install-recommends && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

