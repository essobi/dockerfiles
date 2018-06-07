FROM jlrigau/geth  
  
MAINTAINER Jean-Louis Rigau (jlrigau@xebia.fr)  
  
RUN apt-get update && \  
apt-get install -y cpp-ethereum nodejs npm && \  
apt-get clean  
  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
RUN npm install -g embark-framework grunt-cli  
  
RUN mkdir /dapp  
  
WORKDIR /dapp  
  
ENTRYPOINT ["embark"]

