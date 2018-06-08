FROM mercari/appengine-go:1.8-slim  
  
ARG PROTOC_VERSION=3.4.0  
  
RUN curl -fo protoc.zip -sSL
"https://github.com/google/protobuf/releases/download/v${PROTOC_VERSION}/protoc-${PROTOC_VERSION}-linux-x86_64.zip"
&& \  
mkdir protoc && \  
unzip -q protoc.zip -d protoc && \  
cp ./protoc/bin/protoc /usr/local/bin/ && \  
cp -rf ./protoc/include/google /usr/local/include/ && \  
rm protoc.zip protoc -rf && \  
go get -u github.com/golang/protobuf/protoc-gen-go && \  
rm -rf ${GOPATH}/src/github.com/golang ${GOPATH}/pkg && \  
go get -u github.com/golang/dep/cmd/dep  
  

