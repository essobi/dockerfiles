FROM ubuntu:16.04  
MAINTAINER tools@digital.trade.gov.uk  
  
ENV LIBPNG_VERSION 0_1.2.50-2  
ENV NVM_DIR /usr/local/nvm  
ENV NODE_VERSION 8.11.1  
ENV YARN_VERSION 1.6.0  
ENV NPM_CONFIG_LOGLEVEL info  
ENV DOCKERIZE_VERSION v0.3.0  
# Replace shell with bash so we can source files  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
RUN apt-get update  
  
# Install packages needed by datahub frontend npm dependencies  
RUN apt-get install -y curl \  
wget \  
libssl-dev \  
libpng-dev \  
libgconf-2-4 \  
libxss1 \  
libappindicator1 \  
libindicator7 \  
fonts-liberation  
  
# Install nvm with node and npm  
RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.30.1/install.sh |
bash \  
&& source $NVM_DIR/nvm.sh \  
&& nvm install $NODE_VERSION \  
&& nvm alias default $NODE_VERSION \  
&& nvm use default \  
&& npm install -g yarn@$YARN_VERSION  
  
# Install Java 8  
RUN apt-get install -y openjdk-8-jre  
  
# Install chrome dependencies (for chrome driver to use)  
RUN apt-get install -y xdg-utils \  
libgtk-3-0 \  
lsb-release  
  
# Install chrome  
RUN curl https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb -O  
RUN dpkg -i google-chrome-stable_current_amd64.deb  
RUN rm google-chrome-stable_current_amd64.deb  
  
# Install dockerise  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz  
RUN tar -C /usr/local/bin -xzvf dockerize-linux-
amd64-$DOCKERIZE_VERSION.tar.gz && rm dockerize-linux-
amd64-$DOCKERIZE_VERSION.tar.gz  
  
# Confirm what has been installed  
RUN source $NVM_DIR/nvm.sh \  
&& echo "nodeJs $(node -v)" \  
&& echo "npm $(npm -v)" \  
&& echo "yarn $(yarn -v)" \  
&& java -version \  
&& google-chrome --version  

