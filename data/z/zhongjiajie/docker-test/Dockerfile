FROM python:3.6-slim  
  
ENV NODE_VERSION 6.5.0  
ENV NODE_ROOT /usr/local/nodejs  
  
ENV APP_ROOT /usr/src/app  
  
# ENV CLIENT_HOME /gzdrug-client  
COPY package.json $APP_ROOT/  
  
RUN set -ex \  
&& devTool=' \  
wget \  
vim \  
ssh \  
telnet \  
iputils-ping \  
' \  
&& apt-get update -yqq \  
&& apt-get install -yqq --no-install-recommends \  
ca-certificates \  
$devTool \  
libpng-dev \  
# https://stackoverflow.com/a/14789400/7152658  
rsync \  
git \  
&& wget --no-check-certificate
"https://nodejs.org/download/release/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& mkdir -p $NODE_ROOT \  
&& tar -xvzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C $NODE_ROOT \  
&& mv $NODE_ROOT/node-v$NODE_VERSION-linux-x64 $NODE_ROOT/node$NODE_VERSION \  
&& ln -s $NODE_ROOT/node$NODE_VERSION/bin/node /bin/node \  
&& ln -s $NODE_ROOT/node$NODE_VERSION/bin/npm /bin/npm \  
&& mkdir -p $APP_ROOT/node_modules \  
&& npm install --prefix $APP_ROOT \  
&& rm -rf \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
/usr/share/man \  
/usr/share/doc \  
/usr/share/doc-base \  
/node-v$NODE_VERSION-linux-x64.tar.gz  
  
WORKDIR $APP_ROOT  
  
CMD ["bash"]

