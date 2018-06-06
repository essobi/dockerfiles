FROM lsiobase/alpine:3.7  
# set version label  
ARG BUILD_DATE  
ARG VERSION  
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:-
${BUILD_DATE}"  
LABEL maintainer="sparklyballs"  
# build variables  
ARG GOPATH=/tmp/golang  
ARG CARDIGANN_DIR=$GOPATH/src/github.com/cardigann/cardigann  
  
# environment variables  
ENV CONFIG_DIR=/config  
  
RUN \  
echo "**** install build packages ****" && \  
apk add --no-cache --virtual=build-dependencies \  
g++ \  
gcc \  
git \  
go \  
make \  
nodejs-npm && \  
echo "**** install runtime packages ****" && \  
apk add --no-cache \  
ca-certificates && \  
echo "**** compile cardigann ****" && \  
git clone https://github.com/vidschofelix/cardigann.git ${CARDIGANN_DIR} && \  
git clone https://github.com/creationix/nvm.git /root/.nvm && \  
  
cd ${CARDIGANN_DIR}/web && \  
npm install && \  
cd ${CARDIGANN_DIR} && \  
export PATH=$GOPATH/bin:$PATH && \  
make setup && \  
make test && \  
make build && \  
make install && \  
install -Dm755 \  
$GOPATH/bin/cardigann \  
/usr/bin/cardigann && \  
echo "**** cleanup ****" && \  
apk del --purge \  
build-dependencies && \  
rm -rf \  
/root \  
/tmp/* && \  
mkdir -p \  
/root  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
EXPOSE 5060  
VOLUME /config  

