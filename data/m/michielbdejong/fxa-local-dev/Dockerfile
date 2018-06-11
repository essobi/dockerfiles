FROM ubuntu  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install dependencies  
RUN apt-get update \  
&& apt-get install -y software-properties-common \  
&& add-apt-repository ppa:webupd8team/java \  
&& apt-get update \  
&& echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections \  
&& echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections \  
&& apt-get install -y \  
build-essential \  
git-core \  
graphicsmagick \  
libgmp3-dev \  
oracle-java7-installer \  
python-dev \  
python-virtualenv \  
redis-server \  
wget \  
&& apt-get clean  
  
# Install nvm with node and npm  
RUN git clone https://github.com/creationix/nvm.git /.nvm \  
&& echo ". /.nvm/nvm.sh" >> /etc/bash.bashrc \  
&& /bin/bash -c '. /.nvm/nvm.sh && nvm install v0.10.40 && nvm use v0.10.40 &&
nvm alias default v0.10.40 && ln -s /.nvm/v0.10.40/bin/node /usr/bin/node' \  
&& /.nvm/v0.10.40/bin/npm install -g \  
npm@2 \  
&& ln -s /.nvm/v0.10.40/bin/npm /usr/bin/npm \  
&& /.nvm/v0.10.40/bin/npm install -g \  
node-gyp \  
pm2 \  
&& npm cache clear  
  
# Install fxa-local-dev  
RUN useradd -d /app install  
RUN mkdir /app && chown install /app  
USER install  
RUN cd app && git clone https://github.com/mozilla/fxa-local-dev  
RUN ulimit -S -n 2048 || echo "Setting ulimit failed"  
RUN cd app/fxa-local-dev \  
&& git clone https://github.com/mozilla/fxa-content-server.git \  
&& cd fxa-content-server \  
&& npm i --production \  
&& npm i \  
&& cp server/config/local.json-dist server/config/local.json  
RUN cd app/fxa-local-dev \  
&& git clone https://github.com/mozilla/fxa-auth-server.git \  
&& cd fxa-auth-server \  
&& npm i \  
&& node ./scripts/gen_keys.js  
RUN cd app/fxa-local-dev \  
&& git clone https://github.com/vladikoff/browserid-verifier.git -b http \  
&& cd browserid-verifier \  
&& npm i \  
&& npm i vladikoff/browserid-local-verify#http  
RUN cd app/fxa-local-dev \  
&& git clone https://github.com/mozilla/fxa-oauth-server.git \  
&& cd fxa-oauth-server \  
&& npm i  
RUN cd app/fxa-local-dev \  
&& git clone https://github.com/mozilla/fxa-oauth-console.git \  
&& cd fxa-oauth-console \  
&& npm i  
RUN cd app/fxa-local-dev \  
&& git clone https://github.com/mozilla/fxa-profile-server.git \  
&& cd fxa-profile-server \  
&& npm i \  
&& mkdir -p var/public/  
RUN cd app/fxa-local-dev \  
&& git clone https://github.com/mozilla/fxa-basket-proxy.git \  
&& cd fxa-basket-proxy \  
&& npm i  
RUN cd app/fxa-local-dev \  
&& git clone https://github.com/mozilla/123done.git -b oauth \  
&& cd 123done \  
&& npm i \  
&& CONFIG_123DONE=./config-local.json node ./scripts/gen_keys.js  
RUN cd app/fxa-local-dev \  
&& git clone https://github.com/mozilla-services/loop-server.git \  
&& cd loop-server \  
&& npm i  
RUN cd app/fxa-local-dev \  
&& git clone https://github.com/mozilla-services/syncserver.git \  
&& cd syncserver \  
&& make build  
# This should be fast after previous project-by-project build steps:  
RUN cd app/fxa-local-dev && npm install  
USER root  
  
# Run with pm2  
RUN cd app/fxa-local-dev && pm2 start servers.json  
EXPOSE 3030 1114 10140 9010 9011 1111 1112 1113 8080 10139 10137 5050 6379
10222 5000  
CMD cd app/fxa-local-dev && pm2 start servers.json && pm2 logs  

