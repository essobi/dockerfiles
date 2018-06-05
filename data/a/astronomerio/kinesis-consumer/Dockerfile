FROM java:8  
MAINTAINER Alois Barreras <alois@astronomer.io>  
  
# grab tini for signal processing and zombie killing  
ENV TINI_VERSION v0.9.0  
RUN set -x \  
&& wget -O /usr/local/bin/tini
"https://github.com/krallin/tini/releases/download/$TINI_VERSION/tini" \  
&& wget -O /usr/local/bin/tini.asc
"https://github.com/krallin/tini/releases/download/$TINI_VERSION/tini.asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
6380DC428747F6C393FEACA59A84159D7001A4E5 \  
&& gpg --batch --verify /usr/local/bin/tini.asc /usr/local/bin/tini \  
&& rm -r "$GNUPGHOME" /usr/local/bin/tini.asc \  
&& chmod +x /usr/local/bin/tini \  
&& tini -h  
  
# replace shell with bash so we can source files  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# update the repository sources list  
# and install dependencies  
RUN apt-get update \  
&& apt-get install -y curl apt-transport-https \  
&& apt-get -y autoclean  
  
# nvm environment variables  
ENV NVM_DIR /usr/local/nvm  
ENV NODE_VERSION 7.9.0  
# install nvm  
# https://github.com/creationix/nvm#install-script  
RUN curl --silent -o-
https://raw.githubusercontent.com/creationix/nvm/v0.31.2/install.sh | bash  
  
# install node and npm  
RUN source $NVM_DIR/nvm.sh \  
&& nvm install $NODE_VERSION \  
&& nvm alias default $NODE_VERSION \  
&& nvm use default  
  
# add node and npm to path so the commands are available  
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH  
  
# install yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update && apt-get install yarn  
  
RUN mkdir -p /usr/src/app  
  
RUN mkdir -p /usr/src/app/log  
ENV BUNYAN_LOG_PATH /usr/src/app/log  
  
# Bundle app source  
ONBUILD COPY package.json /usr/src/app  
ONBUILD COPY yarn.lock /usr/src/app  
ONBUILD WORKDIR /usr/src/app  
  
ONBUILD RUN yarn install --production  
ONBUILD COPY lib /usr/src/app/lib  
ONBUILD COPY properties /usr/src/app/properties  
  
ENTRYPOINT ["tini", "--"]  
CMD ["npm", "start"]  

