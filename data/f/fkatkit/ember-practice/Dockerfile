FROM ubuntu:xenial  
  
VOLUME /root/ember  
ADD ./ /root/ember/  
  
# Set env  
ENV HOME="/root" \  
ANYENV_HOME="/root/.anyenv" \  
ANYENV_ENV="/root/.anyenv/envs" \  
PATH="/root/.anyenv/bin:/root/anyenv/env/ndenv/bin:/root/.anyenv/envs/ndenv/shims:$PATH"  
  
# Install anyenv  
RUN \  
rm /bin/sh && ln -s /bin/bash /bin/sh && \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update -y -qq && \  
apt-get upgrade -y -qq && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y byobu curl git htop man unzip vim wget libfontconfig1-dev
automake python-dev && \  
git clone https://github.com/facebook/watchman.git && cd watchman &&
./autogen.sh && ./configure && \  
make && make install && \  
git clone https://github.com/riywo/anyenv $ANYENV_HOME && \  
echo 'export PATH="$HOME/.anyenv/bin:$PATH"' >> ~/.bashrc && \  
echo 'eval "$(anyenv init -)"' >> ~/.bashrc && \  
mkdir $ANYENV_ENV  
  
# Install node.js  
RUN \  
eval "$(anyenv init -)" && \  
anyenv install ndenv && \  
eval "$(anyenv init -)" && \  
ndenv install v6.9.4 && \  
ndenv global v6.9.4 && \  
ndenv rehash && \  
npm config set user 0 && \  
npm config set unsafe-perm true && \  
npm install -g npm && \  
npm install -g bower && \  
npm install -g sm && \  
npm install -g ember-cli@2.11  
  
WORKDIR /root/ember  
  
# Install node.js & build ember.js project  
RUN \  
npm install && \  
eval "$(anyenv init -)" && \  
ember build --environment=development  
  
#################################################################  
# *** When you create a new project, run below RUN commands *** #  
# Create Ember.js project  
# RUN \  
# ember new test-ember  
#################################################################  
  
EXPOSE 4200 49153  
  
CMD ["/root/.anyenv/envs/ndenv/shims/ember", "server", "--host", "0.0.0.0", "
--live-reload-port", "49153"]  

