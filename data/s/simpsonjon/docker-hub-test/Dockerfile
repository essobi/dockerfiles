FROM ubuntu  
  
MAINTAINER Jon Simpson  
ENV HOME=/root  
#Install Node.js  
RUN sudo apt-get update --yes  
  
#ensure required bits  
RUN sudo apt-get install curl git --yes  
  
# download and invoke NVM installer from github  
RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.25.4/install.sh |
HOME=/root sh  
  
# set nvm versions  
ENV NODE_VERSION v0.12.7  
# install stable node and use it  
ENV node /usr/local/bin/node  
RUN curl https://raw.github.com/creationix/nvm/master/install.sh | HOME=/root
sh  
RUN echo '[[ -s /root/.nvm/nvm.sh ]] && . /root/.nvm/nvm.sh' >
/etc/profile.d/nvm.sh  
RUN echo 'nvm install ${NODE_VERSION}' | bash -l  
RUN echo 'nvm alias default ${NODE_VERSION}' | bash -l  
RUN echo 'nvm use ${NODE_VERSION}' | bash -l  
#RUN echo 'test'  
ADD package.json /tmp/package.json  
RUN echo 'cd /tmp && nvm use ${NODE_VERSION} && npm install'  
RUN echo 'cd /tmp && mkdir -p /src && cp -a /tmp/node_modules /src/'  
RUN /bin/bash -c 'ln -s ~/.nvm/versions/node/v0.12.7/bin/node /usr/bin/node &&
ln -s ~/.nvm/versions/node/v0.12.7/bin/npm /usr/bin/npm'  
#RUN . ~/.nvm/nvm.sh && nvm install $NODE_VERSION && nvm alias default
$NODE_VERSION && nvm use $NODE_VERSION \  
# && cd /tmp && npm install \  
# && mkdir -p /src && cp -a /tmp/node_modules /src/  
#RUN /bin/bash -c 'ln -s /home/node/.nvm/v0.12.7/bin/node /usr/bin/node && ln
-s /home/node/.nvm/v0.12.7/bin/npm /usr/bin/npm'  
# set nvm dir  
# Define working directory  
WORKDIR /src  
ADD . /src  
  
# expose port 8080 (default port when running http-server)  
EXPOSE 8080  
# once an instance will be created invoke the run-app script  
CMD ["node", "app.js"]

