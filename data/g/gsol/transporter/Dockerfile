FROM alpine:3.4  
MAINTAINER Global Solutions co., ltd.  
LABEL version="0.1.0"  
  
ENV GOPATH=/go GOVERSION=1.6.3-r0 \  
REPO_NS=github.com/compose \  
PKG_NAME=transporter \  
GODEP=github.com/tools/godep  
ENV PATH=${PATH}:${GOPATH}/bin \  
PKG_NS=${GOPATH}/src/${REPO_NS}  
  
WORKDIR ${PKG_NS}  
RUN apk add --no-cache --virtual .deps git go=${GOVERSION} gcc musl-dev && \  
git clone https://${REPO_NS}/${PKG_NAME} && \  
cd ${PKG_NAME} && \  
go get ${GODEP} && \  
godep restore && godep go build -a ./cmd/... && \  
go get -a ./cmd/... && \  
go clean -i ${GODEP} && \  
cd ${GOPATH} && rm src pkg -rf && \  
apk del .deps  
  
WORKDIR ${GOPATH}/bin  
  
ENTRYPOINT ["transporter"]  

