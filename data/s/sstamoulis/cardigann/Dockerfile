FROM lsiobase/alpine  
  
# Environment variables  
ENV GOPATH=/tmp/golang  
ENV CARDIGANN_DIR=$GOPATH/src/github.com/cardigann/cardigann  
ENV CONFIG_DIR=/config  
  
# install runtime packages  
RUN \  
apk add --no-cache \  
ca-certificates  
  
# install build packages  
RUN \  
apk add --no-cache --virtual=build-dependencies \  
go \  
git \  
make && \  
  
# download and build cardigann  
git clone https://github.com/cardigann/cardigann.git $CARDIGANN_DIR && \  
git -C $CARDIGANN_DIR checkout $(git -C $CARDIGANN_DIR describe --tags
--candidates=1 \--abbrev=0) && \  
make --debug --directory=$CARDIGANN_DIR install && \  
mv $GOPATH/bin/cardigann /usr/bin/cardigann && \  
# cleanup  
apk del --purge \  
build-dependencies && \  
rm -rf /tmp/*  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
EXPOSE 5060  
VOLUME /config  

