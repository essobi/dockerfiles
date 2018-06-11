FROM ros:kinetic-ros-core  
LABEL maintainer="mathieu.lauret30@gmail.com"  
  
COPY client client  
COPY images images  
COPY index.html index.html  
COPY package.json package.json  
COPY server.js server.js  
  
# Install NVM to install nodejs and npm  
# Thanks to remarkablemark and his gist :
https://gist.github.com/remarkablemark/aacf14c29b3f01d6900d13137b21db3a  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y curl=7.47.0-1ubuntu2.8 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV NVM_DIR /usr/local/nvm  
ENV NODE_VERSION 6.12.3  
RUN curl --silent -o-
https://raw.githubusercontent.com/creationix/nvm/v0.31.2/install.sh | bash  
  
RUN /bin/bash -c "source $NVM_DIR/nvm.sh \  
&& nvm install $NODE_VERSION \  
&& nvm alias default $NODE_VERSION \  
&& nvm use default"  
  
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH  
  
RUN npm install  
  
ENTRYPOINT source /opt/ros/kinetic/setup.bash && npm start  
  

