FROM ubuntu:xenial  
  
LABEL MAINTAINER="Daniel Grabert <docker@synec.de>"  
  
# Replace shell with bash so we can source files  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Define nvm version  
ENV NVM_VERSION=0.33.8  
# Define node version  
ENV NODE_VERSION=8.10.0  
# Define nvm base dir  
ENV NVM_DIR=/root/.nvm  
  
# Update apt database  
RUN apt-get update  
# Perform dist-upgrade  
RUN apt-get -y dist-upgrade  
  
# Install deps for building nvm  
RUN apt-get install -y wget build-essential python  
  
# Fetch and install nodejs via nvm  
RUN wget -qO-
https://raw.githubusercontent.com/creationix/nvm/v$NVM_VERSION/install.sh |
bash \  
&& source $NVM_DIR/nvm.sh  
  
# Fetch and install nodejs via nvm  
RUN source $NVM_DIR/nvm.sh \  
&& nvm install $NODE_VERSION \  
&& nvm alias default $NODE_VERSION \  
&& nvm use default  
  
# Export NODE_PATH  
ENV NODE_PATH $NVM_DIR/versions/node/v$NODE_VERSION/lib/node_modules  
  
# Update PATH to make node/npm accessible  
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH  
  
# overwrite this with 'CMD []' in a dependent Dockerfile  
CMD ["/bin/bash"]  

