# VERSION 1.4  
FROM rdpanek/base:2.0  
MAINTAINER Radim Daniel Pánek <rdpanek@gmail.com>  
  
ENV NODEJS_VERSION v4.2.1  
ENV NODEJS_APP node-${NODEJS_VERSION}-linux-x64  
ENV INSTALL_DIR /opt/  
ENV HARNESS_VERSION 0.2.4  
ENV COFFEESCRIPT_VERSION 1.9.3  
ENV WORKSPACE /home/harness/  
  
# Install node & npm  
RUN apt-get update -yq && apt-get upgrade -yq && \  
  
sudo bash - && \  
cd $INSTALL_DIR && curl -L -O
https://nodejs.org/dist/${NODEJS_VERSION}/${NODEJS_APP}.tar.gz && \  
tar -zxvf ${NODEJS_APP}.tar.gz && \  
sudo ln -s $INSTALL_DIR${NODEJS_APP}/bin/npm /usr/bin/npm && \  
sudo ln -s $INSTALL_DIR${NODEJS_APP}/bin/node /usr/bin/node && \  
  
which node; node -v; which npm; npm -v; npm ls -g --depth=0 && \  
  
# Install harness and dependencies  
npm i coffee-script@$COFFEESCRIPT_VERSION -g && \  
npm i test-stack-harness@$HARNESS_VERSION -g && \  
sudo ln -s $INSTALL_DIR${NODEJS_APP}/bin/coffee /usr/bin/coffee && \  
sudo ln -s $INSTALL_DIR${NODEJS_APP}/bin/harness /usr/bin/harness && \  
coffee -v  

