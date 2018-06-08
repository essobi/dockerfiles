FROM golang:latest  
  
ENV ARCH x64  
ENV NODE_VERSION 10.1.0  
ENV YARN_VERSION 1.6.0  
ENV DEP_VERSION 0.4.1  
WORKDIR $GOPATH  
  
# Need xz to install node...  
RUN apt-get update && \  
apt-get install -yqq xz-utils && \  
rm -rf /var/lib/apt/lists/*  
  
# Install node  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-$ARCH.tar.xz" && \  
tar -xJf "node-v$NODE_VERSION-linux-$ARCH.tar.xz" -C /usr/local \--strip-
components=1 --no-same-owner && \  
ln -s /usr/local/bin/node /usr/local/bin/nodejs && \  
rm -f "node-v$NODE_VERSION-linux-$ARCH.tar.xz"  
  
# Install Yarn  
RUN curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" && \  
mkdir -p /opt/yarn && \  
tar -xzf "yarn-v$YARN_VERSION.tar.gz" -C /opt/yarn --strip-components=1 && \  
ln -s /opt/yarn/bin/yarn /usr/local/bin/yarn && \  
ln -s /opt/yarn/bin/yarn /usr/local/bin/yarnpk && \  
rm -f "yarn-v$YARN_VERSION.tar.gz"  
  
# Install go dep  
RUN curl -fSL
"https://github.com/golang/dep/releases/download/v$DEP_VERSION/dep-linux-
amd64" > /usr/local/bin/dep && chmod 755 /usr/local/bin/dep  

