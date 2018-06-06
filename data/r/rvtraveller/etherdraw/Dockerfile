FROM debian:jessie  
  
RUN apt-get update && apt-get install -y \  
libgif-dev \  
libcairo2-dev \  
libpango1.0-dev \  
libjpeg62-turbo-dev \  
git \  
build-essential \  
g++  
  
ENV HOME_DIR=/srv/etherdraw \  
NVM_DIR=/srv/etherdraw/nvm \  
NODE_VERSION=0.12.12  
RUN mkdir $HOME_DIR \  
&& groupadd --gid 6000 etherdraw \  
&& useradd -d $HOME_DIR -r -g etherdraw --uid 6000 etherdraw \  
&& git clone https://github.com/JohnMcLear/draw.git --depth=1 -b develop
$HOME_DIR/draw/ \  
&& curl https://raw.githubusercontent.com/creationix/nvm/v0.31.0/install.sh |
bash \  
&& . $HOME_DIR/nvm/nvm.sh \  
&& nvm install $NODE_VERSION \  
&& nvm alias default $NODE_VERSION \  
&& nvm use default \  
&& $HOME_DIR/draw/bin/installDeps.sh \  
&& mkdir $HOME_DIR/draw/configuration \  
&& ln -s configuration/settings.json settings.json \  
&& chown -R etherdraw:etherdraw $HOME_DIR  
  
ENV NODE_PATH=$NVM_DIR/versions/node/v$NODE_VERSION/lib/node_modules \  
PATH=$NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH  
  
USER etherdraw  
WORKDIR $HOME_DIR/draw  
  
ENTRYPOINT ["node", "/srv/etherdraw/draw/server.js"]  
EXPOSE 9002  

