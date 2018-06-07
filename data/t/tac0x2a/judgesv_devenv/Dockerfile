  
# Base Settings  
FROM ubuntu:14.04  
MAINTAINER TAC tac0x2a  
  
USER root  
  
## packages  
RUN apt-get update -y  
RUN apt-get install curl build-essential libssl-dev -y  
  
## MongoDB  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927  
RUN echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2
multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list  
RUN apt-get update  
RUN apt-get install -y mongodb  
RUN service mongodb start  
  
## change root password  
RUN echo 'root:devenv' |chpasswd # change root password to 'devenv'  
  
## add user 'devenv:devenv'  
RUN useradd -m devenv \  
&& echo "devenv ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \  
&& echo 'devenv:devenv' | chpasswd  
  
# Make devenv  
USER devenv  
WORKDIR /home/devenv  
ENV HOME /home/devenv  
  
# Node.js (nvm)  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.31.0/install.sh | bash  
ENV NODE_VERSION 5.9.0  
ENV NVM_DIR $HOME/.nvm  
RUN . ~/.nvm/nvm.sh && nvm install $NODE_VERSION && nvm alias default
$NODE_VERSION  
# && npm install -g express  
RUN echo ". ~/.nvm/nvm.sh" >> ~/.bashrc  
  
# Application Volumes  
RUN mkdir /home/devenv/work  
  
# Run Application  
ENTRYPOINT sudo service mongodb restart && cd /home/devenv/work && .
~/.nvm/nvm.sh && nvm use $NODE_VERSION && npm install && npm start  

