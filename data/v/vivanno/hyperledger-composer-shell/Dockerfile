FROM ubuntu:xenial  
  
RUN apt update -y  
RUN apt install -y \  
apt-transport-https \  
bash \  
build-essential \  
ca-certificates \  
curl \  
git \  
iputils-ping \  
python \  
software-properties-common \  
sudo \  
telnet  
  
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -  
  
RUN add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \  
$(lsb_release -cs) \  
stable"  
  
RUN apt-get update -y  
RUN apt-get install docker-ce -y  
  
RUN mkdir /home/composer  
RUN groupadd composer  
RUN useradd -u 12345 -g composer -d /home/composer -s /bin/bash -p $(echo
mypasswd | openssl passwd -1 -stdin) composer  
RUN usermod -aG docker composer  
RUN usermod -aG sudo composer  
RUN chown -R composer:composer /home/composer  
  
USER composer  
WORKDIR /home/composer  
  
RUN [ ! -f ~/.bashrc ] && echo "# auto genered bashrc file" > ~/.bashrc  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash  
RUN export NVM_DIR="$HOME/.nvm" && \  
[ -s "$NVM_DIR/nvm.sh" ] && \\. "$NVM_DIR/nvm.sh" && \  
nvm install --lts && \  
npm install -g mkdirp \  
npm install -g composer-cli \  
npm install -g composer-cli \  
npm install -g composer-rest-server \  
npm install -g generator-hyperledger-composer  
  
CMD ["/bin/bash", "-c", "sleep 6000000000000000000"]  

