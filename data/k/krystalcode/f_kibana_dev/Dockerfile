FROM krystalcode/f_nvm  
  
# Install "git", required by "npm" for installing some dependencies.  
RUN dnf -y install git && dnf clean all  
  
ENV NODE_VERSION 0.12.9  
RUN . $HOME/.nvm/nvm.sh && \  
nvm install $NODE_VERSION  
  
# Get the Kibana source code and install its node dependencies.  
RUN mkdir -p /src/kibana && \  
curl -L https://github.com/elastic/kibana/archive/v4.3.1.tar.gz | \  
tar -zxf - -C /src/kibana --strip-components=1 && \  
cd /src/kibana && \  
. $HOME/.nvm/nvm.sh && \  
nvm use $NODE_VERSION && \  
npm install  
  
# Add the Kibana development configuration file.  
ADD ./kibana.dev.yml /src/kibana/config/  
  
WORKDIR /src  
  
# @Issue(  
# "Install the Sense plugin"  
# type="task"  
# priority="normal"  
# )  
EXPOSE 5601  
# @Issue(  
# "Set default node version so that we don't have to do 'nvm use'"  
# type="task"  
# priority="normal"  
# )  
CMD . $HOME/.nvm/nvm.sh && nvm use 0.12.9 && cd /src/kibana && npm start  

