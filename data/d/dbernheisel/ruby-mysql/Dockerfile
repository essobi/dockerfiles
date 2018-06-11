# RUBY  
FROM ruby:2.0.0-p594  
MAINTAINER david.bernheisel@scimedsolutions.com  
  
RUN echo "deb http://repo.mysql.com/apt/debian/ jessie mysql-5.7" >
/etc/apt/sources.list.d/mysql.list  
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys 5072E1F5  
RUN apt-get update  
RUN apt-get install -y debian-archive-keyring mysql-common mysql-client  
  
# NODE  
# Use Bash instead of SH  
RUN apt-get update && apt-get install -y git curl build-essential libssl-dev  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
ENV NVM_DIR /usr/local/.nvm  
  
# Install nvm  
RUN git clone https://github.com/creationix/nvm.git $NVM_DIR && cd $NVM_DIR &&
git checkout `git describe --abbrev=0 --tags`  
  
# Install default version of Node.js  
RUN source $NVM_DIR/nvm.sh && nvm install --lts=boron && nvm use --lts &&
export NODE_VERSION=$(nvm current | egrep -o '[0-9]+.[0-9]+.[0-9]+') && echo
"export NODE_VERSION=$(nvm current | egrep -o '[0-9]+.[0-9]+.[0-9]+')" >>
$HOME/.bashrc && nvm alias default $NODE_VERSION && nvm use default  
  
# Add nvm.sh to .bashrc for startup...  
RUN echo "source ${NVM_DIR}/nvm.sh" > $HOME/.bashrc && source $HOME/.bashrc  
  
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/v$NODE_VERSION/bin:$PATH  

