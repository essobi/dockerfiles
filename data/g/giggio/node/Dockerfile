FROM ubuntu:14.04  
MAINTAINER Giovanni Bassi <giggio@giggio.net>  
  
#install node and build pack defs and python (used by node-gyp)  
ENV NODE_VERSION 0.10.32  
RUN apt-get update \  
&& apt-get install -y \  
curl \  
autoconf \  
build-essential \  
imagemagick \  
libbz2-dev \  
libcurl4-openssl-dev \  
libevent-dev \  
libffi-dev \  
libglib2.0-dev \  
libjpeg-dev \  
libmagickcore-dev \  
libmagickwand-dev \  
libmysqlclient-dev \  
libncurses-dev \  
libpq-dev \  
libpq-dev \  
libreadline-dev \  
libsqlite3-dev \  
libssl-dev \  
libxml2-dev \  
libxslt-dev \  
libyaml-dev \  
zlib1g-dev \  
python \  
git-core  
  
RUN gpg --keyserver pgp.mit.edu --recv-keys
7937DFD2AB06298B2293C3187D33FF9D0246406D  
RUN curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --verify SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc |
sha256sum -c - \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc  
  
#install mongo (only for client use)  
ENV MONGO_VERSION 2.6.4  
RUN gpg --keyserver pgp.mit.edu --recv-keys
DFFA3DCF326E302C4787673A01C4E7FAAAB2461C  
RUN curl -SL "https://fastdl.mongodb.org/linux/mongodb-
linux-x86_64-$MONGO_VERSION.tgz" -o mongo.tgz \  
&& curl -SL "https://fastdl.mongodb.org/linux/mongodb-
linux-x86_64-$MONGO_VERSION.tgz.sig" -o mongo.tgz.sig \  
&& gpg --verify mongo.tgz.sig \  
&& tar -xvf mongo.tgz -C /usr/local \--strip-components=1 \  
&& rm mongo.tgz*  
  
VOLUME /proj  
WORKDIR /proj  
  
#install node tools  
RUN [ "npm", "install", "-g", "bower", "grunt-cli", "coffee-script", "mocha",
"node-inspector", "nodemon", "coffeelint", "js2coffee", "gulp" ]  
  
#expose dev port  
EXPOSE 3000  
EXPOSE 3001  
EXPOSE 3002  
EXPOSE 3003  
#expose debug port  
EXPOSE 5858  
ENTRYPOINT [ "/bin/bash" ]  

