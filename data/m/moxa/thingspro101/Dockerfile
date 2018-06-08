FROM ubuntu:16.04  
ENV NODE_INSTALL_VERSION=${NODE_INSTALL_VERSION:-v6}  
ENV GENERATOR_VERSION=${GENERATOR_VERSION:-latest}  
  
RUN apt-get update && \  
apt-get install -y \  
vim curl git-core build-essential python \  
python-dev sshpass rsync sshfs && \  
rm -rf /var/lib/apt/lists/*  
  
# Install pip  
RUN curl https://bootstrap.pypa.io/get-pip.py | python && \  
pip install -U virtualenv  
  
RUN useradd -ms /bin/bash moxa  
  
USER moxa  
  
WORKDIR /home/moxa  
  
# Install node via nvm  
RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.32.0/install.sh |
bash && \  
export NVM_DIR=/home/moxa/.nvm && \  
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" && \  
nvm install $NODE_INSTALL_VERSION && \  
nvm use $NODE_INSTALL_VERSION && \  
nvm alias default $NODE_INSTALL_VERSION && \  
npm install -g yo generator-sanji-ui@$GENERATOR_VERSION  
  
RUN virtualenv /home/moxa/pyenv && \  
. /home/moxa/pyenv/bin/activate && \  
echo "export PY_DIR=\"/home/moxa/pyenv\"" >> ~/.bashrc && \  
echo "[ -s \"\$PY_DIR/bin/activate\" ] && . \"\$PY_DIR/bin/activate\"" >>
~/.bashrc && \  
pip install sanji paho-mqtt cookiecutter  
  
RUN git config --global url.https://github.com/.insteadOf git://github.com/  
  
ADD docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  

