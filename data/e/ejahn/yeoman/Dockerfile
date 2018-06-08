# pull base image  
FROM ubuntu:16.04  
MAINTAINER Erik Jahn <erik@cmft.io>  
  
# Replace shell with bash so we can source files  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Install updates, get packages  
RUN apt-get update --fix-missing -y -qq  
RUN apt-get install sudo  
RUN sudo apt-get install -y build-essential libssl-dev curl wget software-
properties-common  
  
# Install ruby, python, etc.  
RUN sudo apt-get install -y python git git-core  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
RUN sudo apt-get install -y nodejs  
  
# Install yeoman, generators and dependencies  
RUN sudo npm install -g grunt-cli bower harp@next gulpjs/gulp-cli yo typings
generator-karma generator-angular generator-webapp generator-fountain-webapp
foundation-cli  
  
# Install nvm  
ENV NVM_DIR /usr/local/nvm  
ENV NODE_VERSION 6  
RUN wget -qO- https://raw.githubusercontent.com/xtuple/nvm/master/install.sh |
sudo bash \  
&& source $NVM_DIR/nvm.sh \  
&& nvm install $NODE_VERSION \  
&& nvm alias default $NODE_VERSION \  
&& nvm use default \  
  
ENV NODE_PATH $NVM_DIR/versions/node/v$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH  
  
# install ruby  
RUN sudo apt-add-repository ppa:brightbox/ruby-ng  
RUN sudo apt-get update  
RUN sudo apt-get install -y ruby2.3 ruby2.3-dev  
  
# install compass  
RUN gem install --no-rdoc --no-ri compass  
  
# Add a yeoman user because grunt doesn't like being root  
RUN adduser --disabled-password --gecos "" yeoman; \  
echo "yeoman ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
USER yeoman  
  
# install oh-my-zsh  
RUN sudo apt-get install -y zsh  
RUN sudo sh -c "$(curl -fsSL
https://raw.githubusercontent.com/robbyrussell/oh-my-
zsh/master/tools/install.sh)"  
RUN sudo cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc  
  
# Create a directory for the app  
RUN sudo mkdir -p /app && cd $_  
WORKDIR /app  
  
EXPOSE 9000  
CMD ["zsh"]  

