FROM artburkart/elixir:1.0.5  
MAINTAINER Arthur Burkart <arturkart@gmail.com>  
  
# Set up environment variables  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG C.UTF-8  
ENV PHOENIX_VERSION 1.0.2  
ENV NODE_VERSION 4.1.1  
ENV NPM_VERSION 2.14.0  
# Install inotify-tools for watching files  
RUN apt-get update && apt-get install -y inotify-tools && rm -rf
/var/lib/apt/lists/*  
  
# Install Phoenix from source as well as phoenix mix tools  
RUN git clone \--depth 1 --branch v$PHOENIX_VERSION
https://github.com/phoenixframework/phoenix.git \  
&& cd phoenix && mix local.hex --force && mix local.rebar --force \  
&& mix do deps.get, compile \  
&& mix archive.install
https://github.com/phoenixframework/phoenix/releases/download/v$PHOENIX_VERSION/phoenix_new-$PHOENIX_VERSION.ez
--force  
  
# Verify gpg and sha256: http://nodejs.org/dist/v0.12.5/SHASUMS256.txt.asc  
# gpg keys listed at https://github.com/nodejs/node  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
# Install Node.js and NPM in order to satisfy brunch.io dependencies  
# the snippet below is borrowed from the official nodejs Dockerfile  
# https://registry.hub.docker.com/_/node/  
ADD http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz
/  
ADD http://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc /  
RUN gpg --verify SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc |
sha256sum -c - \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc \  
&& npm install -g npm@"$NPM_VERSION" \  
&& npm cache clear  
  
EXPOSE 4000  
CMD ["bash", "-c", "mix deps.get && mix phoenix.server"]  

