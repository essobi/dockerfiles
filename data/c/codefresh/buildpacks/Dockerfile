FROM ubuntu:14.04  
  
RUN sudo apt-get -q -y update && \  
sudo apt-get -q -y install \  
curl \  
ssh \  
git \  
sshpass && \  
  
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.25.4/install.sh |
bash && \  
  
echo 'export NVM_DIR="/root/.nvm"' >> ~/.bashrc && \  
echo '[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"' >> ~/.bashrc && \  
  
bash -ilc 'nvm install 4.2.2 \  
&& nvm alias 4.2.2 stable \  
&& nvm install iojs \  
&& nvm alias iojs stable \  
&& nvm alias default 4.2.2' && \  
  
bash -ilc 'npm install -g bower grunt-cli gulp && npm cache clean' && \  
  
apt-get clean autoclean && \  
apt-get autoremove -y && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
ENV NVM_BIN /root/.nvm/versions/node/v4.2.2/bin  
ENV PATH $NVM_BIN:$PATH

