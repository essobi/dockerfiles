FROM centos:7 AS env_builder  
  
RUN yum install -y curl git zip  
RUN curl --silent -o-
https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash  
  
ENV NVM_DIR /root/.nvm  
ARG NODE_VERSION=6.11.1  
ARG NPM_VERSION=5.3.0  
RUN source $NVM_DIR/nvm.sh \  
&& nvm install $NODE_VERSION -g \  
&& nvm alias default $NODE_VERSION \  
&& nvm use default  
  
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH  
  
RUN node -v  
RUN npm -v

