FROM debian:jessie-backports  
  
ENV NVM_VERSION v0.33.0  
ENV NODE_VERSION v5.5.0  
ENV NVM_DIR /usr/local/.nvm  
ENV NODE_PATH $NVM_DIR/$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/$NODE_VERSION/bin:$PATH  
  
USER root  
  
ENV HOME /root  
  
RUN apt-get update --yes && apt-get upgrade --yes  
RUN apt-get install -y --no-install-recommends \  
git \  
curl \  
build-essential\  
libssl-dev\  
ca-certificates  
  
# Replace shell with bash so we can source files  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Install nvm  
RUN git clone https://github.com/creationix/nvm.git $NVM_DIR && \  
cd $NVM_DIR && \  
git checkout `git describe --abbrev=0 --tags`  
  
# Install default version of Node.js  
RUN source $NVM_DIR/nvm.sh && \  
nvm install $NODE_VERSION && \  
nvm alias default $NODE_VERSION && \  
nvm use default && \  
touch /root/.bashrc && \  
echo "source ${NVM_DIR}/nvm.sh" > /root/.bashrc && \  
source /root/.bashrc  
  
WORKDIR /opt/grand-central  
  
ADD . /opt/grand-central  
  
RUN source /root/.bashrc && npm install  
  
ENV GRAND_CENTRAL_ENV=production  
  
ENTRYPOINT ["/bin/bash", "--login", "-i", "-c"]  
CMD ["bin/grand-central"]  
  

