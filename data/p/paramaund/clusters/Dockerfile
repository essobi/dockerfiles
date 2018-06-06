FROM ubuntu:16.04  
#ENV RUN_USER daemon  
#ENV RUN_GROUP daemon  
ENV TERM xterm  
ENV DIR /home/daemon/clusters  
ENV NVM_DIR /usr/local/nvm  
ENV NODE_VERSION 7.0.0  
# Set up our PATH correctly so we don't have to long-reference npm, node, &c.  
ENV NODE_PATH ${NVM_DIR}/versions/node/v${NODE_VERSION}/lib/node_modules  
ENV PATH ${NVM_DIR}/versions/node/v${NODE_VERSION}/bin:${PATH}  
  
# Replace shell with bash so we can source files  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
RUN mkdir -p ${DIR} \  
&& apt-get update \  
&& apt-get install build-essential libssl-dev curl -y \  
&& curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.32.1/install.sh | bash \  
&& echo ". ${NVM_DIR}/nvm.sh" >> /etc/bash.bashrc \  
&& source ${NVM_DIR}/nvm.sh \  
&& nvm install ${NODE_VERSION} \  
&& npm i -g nodemon  
  
WORKDIR ${DIR}  
  
ADD . ${DIR}  
  
RUN source ${NVM_DIR}/nvm.sh \  
&& npm i --production  
  
EXPOSE 3000  
#USER ${RUN_USER}:${RUN_GROUP}  
ENTRYPOINT ["npm", "run"]  
  
CMD ["start"]

