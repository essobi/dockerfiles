FROM golang:1.8-alpine  
  
ARG GO_ROOT_IMPORT_PATH=github.com/icedream/workreport-manager  
  
COPY . "/go/src/${GO_ROOT_IMPORT_PATH}"  
RUN \  
apk add \--no-cache --virtual .build-deps \  
git \  
libc-dev \  
&&\  
git config \--global http.followRedirects true &&\  
mkdir -p /go &&\  
export GOPATH=/go &&\  
export PATH="${PATH}:${GOPATH}/bin" &&\  
go get -v \  
github.com/jteeuwen/go-bindata/... \  
golang.org/x/tools/cmd/goimports &&\  
export CGO_ENABLED=0 &&\  
go get -v -d "${GO_ROOT_IMPORT_PATH}/..." &&\  
(cd "${GOPATH}/src/${GO_ROOT_IMPORT_PATH}" &&\  
go generate -v ./...) &&\  
go build -v -a -installsuffix cgo \  
-o /usr/local/bin/workreportmgr "${GO_ROOT_IMPORT_PATH}" &&\  
apk del .build-deps &&\  
rm -rf "${GOPATH}"  
  
ENTRYPOINT ["workreportmgr"]  

