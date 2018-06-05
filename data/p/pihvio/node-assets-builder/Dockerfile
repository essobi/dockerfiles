FROM pihvio/base:debian  
MAINTAINER Onni Hakala <onni@keksi.io>  
  
ARG NVM_VERSION=v0.33.2  
# Replace shell with bash so we can source files  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Install base dependencies  
RUN apt-get update && apt-get install -y -q --no-install-recommends \  
apt-transport-https \  
build-essential \  
ca-certificates \  
curl \  
git \  
libssl-dev \  
python \  
rsync \  
software-properties-common \  
wget \  
  
&& apt-get clean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*
/var/log/apt/* /var/log/*.log  
  
ENV NVM_DIR /usr/local/nvm  
ENV NODE_VERSION v8.1.2  
# Install nvm with node and npm  
RUN curl
https://raw.githubusercontent.com/creationix/nvm/${NVM_VERSION}/install.sh |
bash \  
&& source $NVM_DIR/nvm.sh \  
&& nvm install $NODE_VERSION \  
&& nvm alias default $NODE_VERSION \  
&& nvm use default \  
# Install yarn  
&& npm install -g yarn \  
# Install node-sass, webpack, grunt and gulp globally  
&& yarn global add node-sass webpack grunt gulp bower --global-folder=`yarn
global bin`  
  
ENV ORIG_PATH $PATH  
ENV NODE_PATH $NVM_DIR/$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/$NODE_VERSION/bin:$PATH  
  
# Uses yarn as a default package installer  
ENV PACKAGE_INSTALLER 'yarn'  
# Install custom helper for one command building  
COPY asset-builder.sh /usr/local/bin/asset-builder  
  
# Mount projects in here and run commands here too  
WORKDIR /build  
  
ENTRYPOINT []  
CMD /usr/local/bin/asset-builder

