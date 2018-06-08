FROM buildpack-deps  
  
RUN groupadd -r mongodb && useradd -r -g mongodb mongodb  
  
WORKDIR /src  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv D68FA50FEA312927 && \  
echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.2 main" >
/etc/apt/sources.list.d/mongodb-org.list && \  
apt-get update && \  
apt-get install -y git zlib1g-dev libbz2-dev libsnappy-dev scons numactl gnupg
mongodb-org-tools && \  
rm -rf /var/lib/apt/lists/*  
  
ENV GOSU_VERSION 1.7  
RUN set -x \  
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
  
ENV ROCKSDB_VERSION 4.11.2  
# -j$(nproc)  
RUN wget -O rocksdb-v${ROCKSDB_VERSION}.tar.gz
https://github.com/facebook/rocksdb/archive/v${ROCKSDB_VERSION}.tar.gz && \  
tar xvzf rocksdb-v${ROCKSDB_VERSION}.tar.gz && \  
rm -f rocksdb-v${ROCKSDB_VERSION}.tar.gz && \  
cd rocksdb-${ROCKSDB_VERSION} && \  
CXXFLAGS="-flto -Os -s" make -j$(nproc) --max-load shared_lib && \  
INSTALL_PATH=/usr make install && \  
cd .. && \  
rm -fr rocksdb-${ROCKSDB_VERSION}  
  
ENV MONGO_VERSION 3.2.0  
RUN wget -O mongo-rocks-r${MONGO_VERSION}.tar.gz https://github.com/mongodb-
partners/mongo-rocks/archive/r${MONGO_VERSION}.tar.gz && \  
tar xvzf mongo-rocks-r${MONGO_VERSION}.tar.gz && \  
rm -f mongo-rocks-r${MONGO_VERSION}.tar.gz && \  
git clone -b "r${MONGO_VERSION}" \--single-branch --depth 1
https://github.com/mongodb/mongo.git mongo-r${MONGO_VERSION} && \  
mkdir -p mongo-r${MONGO_VERSION}/src/mongo/db/modules/ && \  
ln -sf /src/mongo-rocks-r${MONGO_VERSION}
mongo-r${MONGO_VERSION}/src/mongo/db/modules/rocks && \  
cd mongo-r${MONGO_VERSION} && \  
CXXFLAGS="-flto -Os -s" scons \  
CPPPATH=/usr/local/include \  
LIBPATH=/usr/local/lib \  
-j$(nproc) \  
\--release \  
\--prefix=/usr \  
\--opt \  
mongod \  
install && \  
cd .. && \  
mkdir -p /data/db /data/configdb && \  
chown -R mongodb:mongodb /data/db /data/configdb && \  
rm -fr mongo-rocks-r${MONGO_VERSION} mongo-r${MONGO_VERSION}  
  
VOLUME /data/db /data/configdb  
  
ENV MONGO_DATABASE dev  
ADD docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 27017  
CMD ["mongod"]  

