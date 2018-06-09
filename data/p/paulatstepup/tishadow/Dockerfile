FROM ubuntu:14.04  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get install -y git curl  
RUN adduser --disabled-password --gecos "" tishadowuser  
USER tishadowuser  
ENV NVM_DIR /home/tishadowuser/node_dir  
RUN mkdir -p /home/tishadowuser/node_dir  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.33.1/install.sh | bash  
ENV NODE_VERSION v6.6.0  
RUN /bin/bash -c "source $NVM_DIR/nvm.sh && nvm install $NODE_VERSION && nvm
use --delete-prefix $NODE_VERSION"  
ENV NODE_PATH $NVM_DIR/versions/node/$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/versions/node/$NODE_VERSION/bin:$PATH  
RUN npm install -g titanium tishadow  
EXPOSE 3000  
CMD ["tishadow", "server"]

