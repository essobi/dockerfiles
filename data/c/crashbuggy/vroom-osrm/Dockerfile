FROM ubuntu:xenial  
  
ENV OSRM_BACKEND_VERSION v5.10.0  
RUN apt-get update && \  
apt-get install -qq \  
build-essential \  
cmake \  
git-core \  
libboost-all-dev \  
libboost-filesystem1.58.0 \  
libboost-iostreams1.58.0 \  
libboost-program-options1.58.0 \  
libboost-regex1.58.0 \  
libboost-system1.58.0 \  
libboost-thread1.58.0 \  
libbz2-dev \  
libexpat1 \  
libgomp1 \  
liblua5.2-dev \  
liblua5.2-0 \  
libluabind-dev \  
libluabind0.9.1v5 \  
libosmpbf-dev \  
libpng16-dev \  
libprotobuf-dev \  
libprotobuf9v5 \  
libprotoc-dev \  
libstxxl-dev \  
libstxxl1v5 \  
libtbb-dev \  
libtbb2 \  
libxml2-dev \  
libzip-dev \  
lua5.2 \  
luajit \  
pkg-config \  
protobuf-compiler && \  
mkdir -p /src && \  
cd /src && \  
git clone --depth 10 --branch $OSRM_BACKEND_VERSION
https://github.com/Project-OSRM/osrm-backend && \  
cd osrm-backend && \  
mkdir -p build && \  
cd build && \  
cmake .. -DCMAKE_BUILD_TYPE=Release && \  
cmake --build . && \  
cmake --build . --target install && \  
mkdir -p /usr/local/share/osrm && \  
cp -a /src/osrm-backend/profiles /usr/local/share/osrm && \  
apt-get purge -qq \  
'*-dev' \  
build-essential \  
cmake \  
git-core \  
krb5-locales \  
make \  
wget && \  
apt-get autoremove --purge -qq && \  
apt-get clean && \  
cd / && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /src  
  
ENV VROOM_BRANCH master  
RUN mkdir -p /src && \  
cd /src && \  
apt-get update && \  
apt-get install -qq \  
build-essential \  
g++ \  
git-core \  
libboost-iostreams1.58-dev \  
libboost-iostreams1.58.0 \  
libboost-log-dev \  
libboost-log1.58.0 \  
libboost-regex-dev \  
libboost-system-dev \  
libboost-thread-dev \  
libtbb-dev \  
libtbb2 \  
make \  
pkg-config && \  
git clone --depth 10 --branch $VROOM_BRANCH https://github.com/VROOM-
Project/vroom.git && \  
mkdir -p /src/vroom/bin && \  
cd /src/vroom/src && \  
make && \  
cp /src/vroom/bin/vroom /usr/local/bin && \  
apt-get purge -qq \  
'*-dev' \  
build-essential \  
git-core \  
make && \  
apt-get autoremove --purge -qq && \  
apt-get clean && \  
cd / && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /src  
  
ENV VROOM_EXPRESS_BRANCH master  
RUN apt-get update && \  
apt-get install -qq \  
build-essential \  
git-core \  
npm \  
nodejs-legacy && \  
cd / && \  
git clone --depth 10 --branch $VROOM_EXPRESS_BRANCH https://github.com/VROOM-
Project/vroom-express.git && \  
cd vroom-express && \  
ln -s /dev/stdout access.log && \  
npm install && \  
apt-get purge -qq \  
build-essential \  
git-core \  
make && \  
apt-get autoremove --purge -qq && \  
apt-get clean && \  
cd / && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /src  
  
ENV VROOM_FRONTEND_BRANCH master  
RUN apt-get update && \  
apt-get install -qq \  
build-essential \  
git-core \  
npm \  
nodejs-legacy && \  
cd / && \  
git clone --depth 10 --branch $VROOM_FRONTEND_BRANCH https://github.com/VROOM-
Project/vroom-frontend.git && \  
cd vroom-frontend && \  
npm install && \  
cd /vroom-frontend/src && \  
make && \  
apt-get purge -qq \  
build-essential \  
git-core \  
make && \  
apt-get autoremove --purge -qq && \  
apt-get clean && \  
cd / && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /src  
  
# copied from postgres dockerfile  
ENV GOSU_VERSION 1.10  
RUN set -x \  
&& apt-get update && apt-get install -qq --no-install-recommends ca-
certificates wget && rm -rf /var/lib/apt/lists/* \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true  
  
RUN apt-get update && \  
apt-get install -qq \  
curl \  
iproute \  
iputils-ping \  
nginx \  
supervisor \  
wget && \  
apt-get clean && \  
cd / && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /src  
  
COPY osrm.sh /usr/local/bin  
COPY vroom-express.sh /usr/local/bin  
COPY nginx.sh /usr/local/bin  
COPY start.sh /usr/local/bin  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
VOLUME /osm  
  
EXPOSE 5000  
EXPOSE 3000  
  
ENTRYPOINT ["/usr/local/bin/start.sh"]  

