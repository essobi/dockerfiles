FROM node:4.8.7-slim  
  
RUN apt-get update && \  
apt-get install -y \  
g++ \  
libzmq3-dev \  
libzmq3-dbg \  
libzmq3 \  
make \  
python \  
gettext-base \  
jq \  
patch \  
&& \  
wget https://github.com/Yelp/dumb-init/releases/download/v1.2.1/dumb-
init_1.2.1_amd64.deb && \  
dpkg -i dumb-init_*.deb  
  
EXPOSE 3001 3232 9999 19999  
WORKDIR /root/dash-node  
COPY bitcore-node ./  
RUN npm config set package-lock false && \  
npm install && \  
ln -s /root/.bitcore/data/dashd ./dashd && \  
cat logo-insight-dash.patch | patch -p1 -d node_modules/insight-ui-dash  
  
RUN apt-get purge -y \  
g++ make python gcc && \  
apt-get autoclean && \  
apt-get autoremove -y && \  
rm -rf \  
node_modules/bitcore-node-dash/test \  
/root/.bitcore/data/dashcore-*/bin/dash-qt \  
/root/.bitcore/data/dashcore-*/bin/test_dash \  
/root/.bitcore/data/dashcore-*-linux64.tar.gz \  
/dumb-init_*.deb \  
/root/.npm \  
/root/.node-gyp \  
/tmp/* \  
/var/lib/apt/lists/*  
  
ENV DASH_LIVENET 0  
ENV API_ROUTE_PREFIX "api"  
ENV UI_ROUTE_PREFIX ""  
ENV API_CACHE_ENABLE 1  
ENV API_LIMIT_ENABLE 1  
ENV API_LIMIT_WHITELIST "127.0.0.1 ::1"  
ENV API_LIMIT_BLACKLIST ""  
ENV API_LIMIT_COUNT 10800  
ENV API_LIMIT_INTERVAL 10800000  
ENV API_LIMIT_WHITELIST_COUNT 108000  
ENV API_LIMIT_WHITELIST_INTERVAL 10800000  
ENV API_LIMIT_BLACKLIST_COUNT 0  
ENV API_LIMIT_BLACKLIST_INTERVAL 10800000  
HEALTHCHECK \--interval=5s --timeout=5s --retries=5 CMD curl -s
"http://localhost:3001/{$API_ROUTE_PREFIX}/sync" | jq -r -e
".status==\"finished\""  
  
ENTRYPOINT ["/usr/bin/dumb-init", "--", "./bitcore-node-entrypoint.sh"]  
  
VOLUME /root/dash-node/data  

