FROM alpine:3.7  
ENV CLAIR_SCANNER_GIT "https://github.com/arminc/clair-scanner.git"  
ENV CLAIR_SCANNER_VERSION "v8"  
ARG RUNTIME_DEPS="docker"  
ARG BUILD_DEPS="make go musl-dev git"  
ARG GO_PATH="/go"  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories && \  
apk update && \  
apk upgrade && \  
apk add --no-cache ${RUNTIME_DEPS} && \  
apk add --no-cache --virtual build-dependencies ${BUILD_DEPS} && \  
export GOPATH=${GO_PATH} && \  
export PATH=${GOPATH}/bin:${PATH} && \  
mkdir -p ${GOPATH}/src ${GOPATH}/bin && \  
cd ${GOPATH}/src && \  
git clone ${CLAIR_SCANNER_GIT} && \  
cd clair-scanner && \  
git checkout ${CLAIR_SCANNER_VERSION} && \  
go get -u github.com/golang/dep/cmd/dep && \  
make ensure && \  
make build && \  
cp clair-scanner /usr/local/bin/clair-scanner && \  
apk del build-dependencies && \  
rm -rf /var/cache/apk/* /tmp/* ${GOPATH}  
  
ENTRYPOINT ["/usr/local/bin/clair-scanner"]  

