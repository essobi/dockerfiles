# Pull down dumb-init to use later  
FROM gcr.io/cloud-builders/wget AS dumb-init  
ARG DUMB_INIT_VER=1.2.0  
RUN wget -O /dumb-init https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VER}/dumb-init_${DUMB_INIT_VER}_amd64  
  
FROM golang:1.9.2-stretch AS strata  
  
# Install strata  
RUN set -ex; \  
go get github.com/facebookgo/rocks-strata/strata; \  
go get github.com/AdRoll/goamz/s3; \  
go get github.com/AdRoll/goamz/s3/s3test; \  
go get github.com/Azure/azure-sdk-for-go/storage; \  
go get github.com/facebookgo/mgotest; \  
go get github.com/minio/minio-go; \  
go get gopkg.in/mgo.v2; \  
go get gopkg.in/mgo.v2/bson; \  
cd ${GOPATH}/src/github.com/facebookgo/rocks-
strata/strata/cmd/mongo/lreplica_drivers/strata; \  
go build; \  
cp strata /usr/local/bin;  
  
FROM debian:stretch-slim AS mongo-rocksdb  
  
# Install packages deps  
RUN set -ex; \  
apt-get update; \  
apt-get -qq -y --no-install-recommends install \  
zlib1g-dev libbz2-dev libsnappy-dev git \  
python-pkg-resources python-cheetah python-pip python-yaml scons build-
essential  
  
ENV ROCKSDB_VERSION=5.8.8 \  
MONGODB_VERSION=3.6.0  
ARG SOURCE_DIR=/src  
ADD https://github.com/facebook/rocksdb/archive/v${ROCKSDB_VERSION}.tar.gz
${SOURCE_DIR}/rocksdb/  
ADD https://github.com/mongodb/mongo/archive/r${MONGODB_VERSION}.tar.gz
${SOURCE_DIR}/mongo/  
ADD https://github.com/mongodb-partners/mongo-
rocks/archive/r${MONGODB_VERSION}.tar.gz ${SOURCE_DIR}/mongo-rocks/  
  
# Install mongo-rocksdb  
RUN set -ex; \  
cd ${SOURCE_DIR}/rocksdb; \  
tar -zxf v${ROCKSDB_VERSION}.tar.gz --strip-components=1; \  
USE_RTTI=1 CFLAGS=-fPIC make static_lib; \  
INSTALL_PATH=/usr make install; \  
INSTALL_PATH=/opt/rocksdb make install; \  
cd ..; \  
cd ${SOURCE_DIR}/mongo; \  
tar -zxf r${MONGODB_VERSION}.tar.gz --strip-components=1; \  
cd ${SOURCE_DIR}/mongo-rocks; \  
tar -zxf r${MONGODB_VERSION}.tar.gz --strip-components=1; \  
mkdir -p ${SOURCE_DIR}/mongo/src/mongo/db/modules/; \  
ln -sf ${SOURCE_DIR}/mongo-rocks
${SOURCE_DIR}/mongo/src/mongo/db/modules/rocks; \  
pip install typing;  
  
RUN set -ex; \  
cd ${SOURCE_DIR}/mongo; \  
scons MONGO_VERSION=${MONGODB_VERSION};  
  
# https://github.com/gperftools/gperftools/issues/693  
# This blocks us from using alpine linux  
# The sha is for stretch_slim  
FROM
debian@sha256:50a283f43b55f68914da6282263bf81f1e440b6d10565072ef5abd3673df29e8  
ARG HOME=/app  
WORKDIR ${HOME}  
  
COPY \--from=strata /usr/local/bin/strata /usr/local/bin/strata  
COPY \--from=mongo-rocksdb /usr/local/bin/mongod /usr/local/bin/mongod  
COPY \--from=mongo-rocksdb /opt/rocksdb/include/rocksdb /usr/include/rocksdb  
COPY \--from=mongo-rocksdb /opt/rocksdb/lib/librocksdb.a /usr/lib/librocksdb.a  
COPY \--from=dumb-init /dumb-init /usr/local/bin/dumb-init  
RUN chmod +x /usr/local/bin/dumb-init  
  
ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]  

