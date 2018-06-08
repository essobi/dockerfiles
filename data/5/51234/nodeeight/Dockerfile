FROM eclipse/stack-base:debian  
  
ENV NVM_VERSION=v0.33.8  
ENV NODE_VERSION=v8.9.4  
ENV NVM_DIR=$HOME/.nvm  
  
RUN sudo apt-get update && \  
sudo apt-get -y install build-essential libkrb5-dev gcc make apt-transport-
https && \  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add \- && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee
/etc/apt/sources.list.d/yarn.list && \  
curl -o\-
https://raw.githubusercontent.com/creationix/nvm/${NVM_VERSION}/install.sh |
bash && \  
/bin/bash -i -c "source $NVM_DIR/nvm.sh && nvm alias default $NODE_VERSION &&
nvm use --delete-prefix $NODE_VERSION" && \  
bash -c 'source $HOME/.nvm/nvm.sh && \  
npm i -g pug-cli diff2html bower live-server http-server npm-gui npm-home
npmvet cost-of-modules bower-browser mocha-cli mocha speedtest && \  
npm install --prefix "$HOME/.nvm/"' && \  
sudo apt-get update && \  
sudo apt-get install -y ruby-full rubygems debian-keyring python2.7 ca-
certificates yarn && \  
# sudo gem install -​-no-document sass:3.4.22 && \  
# sudo gem install -​-no-document compass && \  
sudo gem install sass:3.4.22 && \  
sudo gem install compass && \  
sudo apt-get -y autoremove && \  
sudo apt-get -y clean && \  
sudo rm -rf /var/lib/apt/lists/*  
  
# following npmjs advice on how to avoid EACCESS errors:
https://github.com/creationix/nvm/blob/master/README.md#installation  
  
# RUN npm i -g pug-cli diff2html live-server npm-gui npm-home npmvet cost-of-
modules bower-browser mocha mocha-cli mochawesome speedtest  
# RUN sudo rm /bin/sh && sudo ln -s /bin/bash /bin/sh  
# ENV NODE_PATH=$NVM_DIR/v$NODE_VERSION/lib/node_modules  
# ENV PATH=$NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH  
# RUN wget -qO- https://deb.nodesource.com/setup_8.x | sudo -E bash -  
# RUN sudo apt update && sudo apt -y install nodejs  
# RUN sudo apt-get install -y build-essential  
  
#RUN curl -o\-
https://raw.githubusercontent.com/creationix/nvm/${NVM_VERSION}/install.sh |
bash  
#RUN /bin/bash -i -c "source $NVM_DIR/nvm.sh && nvm alias default
$NODE_VERSION && nvm use --delete-prefix $NODE_VERSION"  
#RUN bash -c 'source $HOME/.nvm/nvm.sh && \  
# npm i -g pug-cli diff2html bower live-server http-server npm-gui npm-home
npmvet cost-of-modules bower-browser mocha-cli mocha speedtest && \  
# npm install --prefix "$HOME/.nvm/"'  
  
EXPOSE 1337 3000 4200 5000 9000 8003  
  
# -"npm i" is failing.- /home/user/ does not exist  
# RUN sudo chown -R $USER:$(id -gn $USER) /home/user/.config  
  
LABEL che:server:8003:ref=angular che:server:8003:protocol=http
che:server:3000:ref=node-3000 che:server:3000:protocol=http
che:server:9000:ref=node-9000 che:server:9000:protocol=http  

