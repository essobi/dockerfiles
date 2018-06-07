FROM josephyi/elixir-dev:latest  
  
MAINTAINER Joseph Yi <joe@josephyi.com>  
  
# Borrowed node install from smebberson/alpine-nodejs  
ENV NODE_VERSION=v7.7.3 NPM_VERSION=4.4.4  
RUN mkdir -p /etc/ssl/certs && apk -U add ca-certificates && update-ca-
certificates  
RUN apk add --update inotify-tools git curl make gcc g++ python linux-headers
libgcc libstdc++ binutils-gold && \  
cd / && \  
curl -sSL https://nodejs.org/dist/${NODE_VERSION}/node-${NODE_VERSION}.tar.gz
| tar -xz && \  
cd /node-${NODE_VERSION} && \  
./configure --prefix=/usr --without-snapshot && \  
make -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) && \  
make install && \  
cd / && \  
npm install -g npm@${NPM_VERSION} && \  
npm install -g yarn && \  
apk del gcc g++ linux-headers binutils-gold && \  
rm -rf /etc/ssl /node-${NODE_VERSION} /usr/include \  
/usr/share/man /tmp/* /var/cache/apk/* /root/.npm /root/.node-gyp \  
/usr/lib/node_modules/npm/man /usr/lib/node_modules/npm/doc
/usr/lib/node_modules/npm/html  
  
ENV PHOENIX_VERSION=1.2.0  
RUN mix local.hex --force && \  
mix local.rebar --force  
RUN mix archive.install
https://github.com/phoenixframework/archives/raw/master/phoenix_new-${PHOENIX_VERSION}.ez
--force  
  
EXPOSE 4000  
VOLUME ["/app"]  
WORKDIR /app  

